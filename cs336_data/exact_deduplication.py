import os
import hashlib

def hash128(line: str) -> int:
    """Return a 128-bit integer hash of the input string."""
    d = hashlib.blake2b(line.encode("utf-8"), digest_size=16)  
    return int.from_bytes(d.digest(), "big")


def exact_line_deduplication(input_files: list[os.PathLike], output_directory: os.PathLike):
    hash_counts = {}
    for input_file in input_files:
        with open(input_file, "r") as f:
            lines = f.readlines()
        for line in lines:
            hash = hash128(line)
            if hash not in hash_counts:
                hash_counts[hash] = 0
            hash_counts[hash] += 1

    for input_file in input_files:
        with open(input_file, "r") as f:
            lines = f.readlines()
        unique_lines = []
        for line in lines:
            hash = hash128(line)
            if hash_counts[hash] == 1:
                unique_lines.append(line)
        with open(output_directory / input_file.name, "w") as f:
            f.writelines(unique_lines)


