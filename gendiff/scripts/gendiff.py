#!/usr/bin/env python
import argparse
import json
import yaml
from gendiff.core.comparator import compare
from typing import Tuple


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--FORMAT', help='set format of output')
    args = parser.parse_args()
    print(args.accumulate(args))


def load_json(file_path1: str, file_path2: str) -> Tuple[dict, dict]:
    with open(file_path1, "r") as file1:
        json1: dict = json.load(file1)
    with open(file_path2, "r") as file2:
        json2: dict = json.load(file2)
    return json1, json2


def load_yaml(file_path1: str, file_path2: str) -> Tuple[dict, dict]:
    with open(file_path1, "r") as file1:
        yml1: dict = yaml.safe_load(file1)
    with open(file_path2, "r") as file2:
        yml2: dict = yaml.safe_load(file2)
    return yml1, yml2


def generate_diff(file_path1: str, file_path2: str) -> str:
    if file_path1.endswith(".json"):
        return compare(*load_json(file_path1, file_path2))
    elif file_path1.endswith(".yml") or file_path1.endswith(".yaml"):
        return compare(*load_yaml(file_path1, file_path2))
    return ""


if __name__ == '__main__':
    main()
