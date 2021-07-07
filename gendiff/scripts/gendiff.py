#!/usr/bin/env python
import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args = parser.parse_args()
    print(args.accumulate(args))


if __name__ == '__main__':
    main()
