#!/usr/bin/env python
import argparse
from gendiff.generator import JSON, PLAIN, STYLISH, generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f',
                        '--format',
                        choices=[STYLISH, PLAIN, JSON],
                        default=STYLISH,
                        help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file,
                        args.second_file,
                        args.format))


if __name__ == '__main__':
    main()
