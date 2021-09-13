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


def generate_diff(file_path1, file_path2):
    res = "{\n"
    json1 = json.load(open(file_path1))
    json2 = json.load(open(file_path2))
    for key1, value1 in sorted(json1.items()):
        for key2, value2 in sorted(json.items()):
            if value1 != json2[key1]:
                res += "  "
    res += "\n}  "
    return res


if __name__ == '__main__':
    main()
