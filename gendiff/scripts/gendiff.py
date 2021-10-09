#!/usr/bin/env python
import argparse
from json import load
from yaml import safe_load
from gendiff.core.comparator import compare_dictionaries
from gendiff.output import plain, stylish, json
from typing import Tuple, Union


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return generate_diff(args['first_file'],
                         args['second_file'],
                         args['format'])


def load_files(file1: str, file2: str, load_func) -> Tuple[dict, dict]:
    with open(file1, "r") as f1:
        with open(file2, "r") as f2:
            return load_func(f1), load_func(f2)


def show_diff(difference: dict, format: str) -> str:
    if format == 'plain':
        return plain.stringify(difference)
    elif format == 'json':
        return json.stringify(difference)
    return stylish.stringify(difference)


def generate_diff(file1: str, file2: str, format='') -> Union[str, None]:
    if file1.endswith(".json"):
        difference = compare_dictionaries(
            *load_files(file1, file2, load))
    elif file1.endswith(".yml") or file1.endswith(".yaml"):
        difference = compare_dictionaries(
            *load_files(file1, file2, safe_load))
    else:
        raise Exception("wrong data format")
    return show_diff(difference, format)


if __name__ == '__main__':
    main()
