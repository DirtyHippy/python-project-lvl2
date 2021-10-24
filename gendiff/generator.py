import os
from json import load
from yaml import safe_load
from gendiff.comparator import compare_dictionaries
from gendiff.output import plain, stylish, json
from typing import Dict


STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'


def load_file(file: str) -> dict:
    file_ext = os.path.splitext(file)[1].lower()
    if file_ext == ".json":
        with open(file, "r") as f:
            return load(f)
    elif file_ext == ".yml" or file_ext == ".yaml":
        with open(file, "r") as f:
            return safe_load(f)
    else:
        raise Exception("wrong data format")


def get_diff(difference: Dict[str, list], format: str) -> str:
    if format == PLAIN:
        return plain.format(difference)
    elif format == JSON:
        return json.format(difference)
    elif format == STYLISH:
        return stylish.format(difference)
    else:
        raise Exception("wrong format")


def generate_diff(file1: str, file2: str, format=STYLISH) -> str:
    difference = compare_dictionaries(load_file(file1), load_file(file2))
    return get_diff(difference, format)
