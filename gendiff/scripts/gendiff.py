#!/usr/bin/env python
"""Main program."""
from gendiff import generate_diff
from gendiff import get_args


def main():
    args = get_args()
    print(type(args))
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
