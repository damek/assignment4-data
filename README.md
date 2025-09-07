# CS336 Spring 2025 Assignment 4: Data

Follow along on [twitter](https://x.com/damekdavis/status/1963789763309191250)

## Problems

- Looking at common crawl 
  - Download warc and wet files: [look_at_cc.sh](./cs336_data/look_at_cc.sh)
  - Writeup: [look_at_cc.md](./cs336_data/outputs/look_at_cc.md)
- Extract text from warc file: [extract_text.py](./cs336_data/extract_text.py)
  - Writeup: [extract_text.md](./cs336_data/outputs/extract_text.md)
- Language identification: 
  - Code: [language_identification.py](./cs336_data/language_identification.py)
  - Writeup: [language_identification.md](./cs336_data/outputs/language_identification.md)
- Mask PII:
  - Code: [mask_pii.py](./cs336_data/mask_pii.py)
  - Writeup: [mask_pii.md](./cs336_data/outputs/mask_pii.md)
- Harmful content:
  - Code: [harmful_content.py](./cs336_data/harmful_content.py)
  - Writeup: [harmful_content.md](./cs336_data/outputs/harmful_content.md)
- Gopher quality filters:
  - Code: [gopher_quality_filters.py](./cs336_data/gopher_quality_filters.py)
  - Writeup: [gopher_quality_filters.md](./cs336_data/outputs/gopher_quality_filters.md)
- Quality classifier: trained on 5000 outbound wiki links and 5000 cc samples.
  - Code: [quality_classifier.py](./cs336_data/quality_classifier.py)
- Exactly removing all lines that appear more than once in the corpus:
  - Code: [exact_deduplication.py](./cs336_data/exact_deduplication.py)
- Minhash deduplication:
  - Code: [minhash_deduplication.py](./cs336_data/minhash_deduplication.py)

## How to run my code 

```bash
runai submit cs336-dev \ -p <user> \  -i nvcr.io/nvidia/pytorch:25.06-py3 \  -g 1 --interactive --attach \  --command -- bash # replace -g 1 with -g 4 for 4 GPUs.
git clone https://github.com/damek/assignment4-data.git
pip install uv
cd assignment4-data
export PATH="$HOME/.local/bin:$PATH"
uv sync
uv venv
source .venv/bin/activate
uv sync
```

## Assignment Description

For a full description of the assignment, see the assignment handout at
[cs336_spring2025_assignment4_data.pdf](./cs336_spring2025_assignment4_data.pdf)

If you see any issues with the assignment handout or code, please feel free to
raise a GitHub issue or open a pull request with a fix.

## Setup

This directory is organized as follows:

- [`./cs336-basics`](./cs336-basics): directory containing a module
  `cs336_basics` and its associated `pyproject.toml`. This module contains the staff 
  implementation of the language model from assignment 1. You will use this training code
  to train an LM on your filtered data. You should not modify the training logic, since
  your leaderboard submission must use it exactly.
- [`./cs336_data`](./cs336_data): This folder is basically empty! This is the
  module where you will implement code to filter and process the data.

Visually, it should look something like:

``` sh
.
├── cs336_basics  # A python module named cs336_basics
│   └── ... an optimized training implementation ...
├── cs336_data  # TODO(you): code that you'll write for assignment 4
│   ├── __init__.py
│   └── ... TODO(you): any other files or folders you need for assignment 4 ...
├── README.md
├── pyproject.toml
└── ... TODO(you): other files or folders you need for assignment 4 ...
```

As in previous assignments, we use `uv` to manage dependencies.

## Submitting

To submit, run `./test_and_make_submission.sh` . This script will install your
code's dependencies, run tests, and create a gzipped tarball with the output. We
should be able to unzip your submitted tarball and run
`./test_and_make_submission.sh` to verify your test results.