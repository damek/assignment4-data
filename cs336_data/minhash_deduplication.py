import os
import random
import mmh3
import re
import string
import unicodedata
import nltk
from nltk.tokenize import word_tokenize

_WS = re.compile(r"\s+")

def murmur128(s: str, seed: int = 0) -> int:
    # 128-bit unsigned hash (as Python int)
    return mmh3.hash128(s, seed=seed, signed=False)

#gpt 5 written.
def normalize_text(text: str) -> str:
    s = text.casefold()
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = "".join(ch for ch in s if not unicodedata.category(ch).startswith("P"))
    s = _WS.sub(" ", s).strip()
    return unicodedata.normalize("NFC", s)

def make_ngrams(text: str, ngrams: int) -> dict[str, int]:
    words = word_tokenize(text)
    for i in range(len(words) - ngrams + 1):
        ngram = " ".join(words[i:i+ngrams])
        ngrams[ngram] = ngrams.get(ngram, 0) + 1
    return ngrams

def make_minhash_signature_for_ngrams(dict_of_ngrams: dict[str, int], num_hashes: int, seed: int = 0) -> list[int]:
    INF = (1 << 128) - 1
    signature = [INF] * num_hashes
    for i in range(num_hashes):
        for ngram in dict_of_ngrams.keys():
            h = murmur128(ngram, seed + i)
            if h < signature[i]:
                signature[i] = h
    return signature

def make_lsh_buckets(signature: list[int], num_bands: int) -> list[list[int]]:
    length_of_band = len(signature) // num_bands
    buckets = [signature[i*length_of_band:(i+1)*length_of_band] for i in range(num_bands)]
    return buckets

def check_if_some_band_matches(bucket1: list[int], bucket2: list[int]) -> bool:
    for i in range(len(bucket1)):
        if bucket1[i] == bucket2[i]:
            return True
    return False


def compute_jaccard_similarity(n_gram_dict1: dict[str, int], n_gram_dict2: dict[str, int]) -> float:
    return len(set(n_gram_dict1) & set(n_gram_dict2)) / len(set(n_gram_dict1) | set(n_gram_dict2))

# gpt 5 written.
def get_connected_components(adj: dict[int, set[int]], n: int) -> list[list[int]]:
    seen, comps = set(), []
    for s in range(n):
        if s in seen: 
            continue
        stack, comp = [s], []
        seen.add(s)
        while stack:
            u = stack.pop()
            comp.append(u)
            for v in adj.get(u, ()):
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        comps.append(comp)
    return comps

def minhash_deduplication(input_files: list[os.PathLike], output_directory: os.PathLike, num_hashes: int, num_bands: int, ngrams: int, jaccard_threshold: float):
    assert num_hashes % num_bands == 0

    # first pass build the entire database of minhash signatures for each file 
    buckets_database = []
    n_gram_dict_database = []
    for input_file in input_files:
        with open(input_file, "r") as f:
            text = f.read()
            normalized_text = normalize_text(text)
            dict_of_ngrams = make_ngrams(normalized_text, ngrams)
            signature = make_minhash_signature_for_ngrams(dict_of_ngrams, num_hashes)
            n_gram_dict_database.append(dict_of_ngrams)
            buckets = make_lsh_buckets(signature, num_bands)
            buckets_database.append(buckets)
    # second pass use LSH to build clusters. 
    # two documents are in the same cluster if they have at least one band in common. 
    clusters : dict[int, set[int]] = {}
    for i in range(len(buckets_database)):
        for j in range(i+1, len(buckets_database)):
            if check_if_some_band_matches(buckets_database[i], buckets_database[j]):
                # check if jaccard similarity is greater than the threshold
                if compute_jaccard_similarity(n_gram_dict_database[i], n_gram_dict_database[j]) >= jaccard_threshold:
                    clusters[j].add(i)
                    clusters[i].add(j)
    # third pass compute jaccard similarity for each cluster and remove duplicates. 
    connected_components = get_connected_components(clusters, len(input_files))
    # For each cluster, sample one document to keep and write to output directory. 
    for cluster in connected_components:
        i = random.choice(cluster)
        with open(output_directory / input_files[i].name, "w") as f:
            with open(input_files[i], "r") as g:
                f.write(g.read())
    return connected_components
