![Python checks](https://github.com/leakquicked/json-inspector/actions/workflows/python-checks.yml/badge.svg)

# JSON Inspector

Validate a local JSON document and summarize its top-level structure.

## Requirements
Python 3.10+, standard library only.

## Usage
`python json_inspector.py --help`

Processes local files only; no network requests or uploads. Do not publish confidential inventories.

## Tests
`python -m unittest discover -s tests -v`
