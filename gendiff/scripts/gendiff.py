#!/usr/bin/env python
import argparse
import json


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--FORMAT', help='set format of output')
    args = parser.parse_args()
    print(args.accumulate(args))


def generate_diff(file_path1: str, file_path2: str) -> str:
    res = "{\n"
    values = list()
    with open(file_path1, "r") as file1:
        json1: dict = json.load(file1)
    with open(file_path2, "r") as file2:
        json2: dict = json.load(file2)
    keys = sorted(set(list(json1.keys()) + list(json2.keys())))
    for key in keys:
        if key in json1 and key in json2:
            if json1[key] != json2[key]:
                values.append("- {}: {}\n".format(key, json1[key]))
                values.append("+ {}: {}\n".format(key, json2[key]))
            else:
                values.append("  {}: {}\n".format(key, json1[key]))
        elif key in json1:
            values.append("- {}: {}\n".format(key, json1[key]))
        else:
            values.append("+ {}: {}\n".format(key, json2[key]))
    res += "  " + "  ".join(values)
    res += "}"
    return res


if __name__ == '__main__':
    main()
