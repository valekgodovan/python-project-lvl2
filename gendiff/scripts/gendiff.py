#!/usr/bin/env python
"""Main program."""
import argparse
import json

def get_file(name_file):
    file = json.load(open(name_file))
    return file

def get_diff(file1, file2) -> str:
    file1_dict = get_file(file1)
    file2_dict = get_file(file2)
    keys = file1_dict.keys() | file2_dict.keys()
    merge_dict = {}
    for v in keys:
        merge_dict[v] = [file1_dict.get(v, []), file2_dict.get(v, [])]
    return merge_dict


def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    print(get_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
