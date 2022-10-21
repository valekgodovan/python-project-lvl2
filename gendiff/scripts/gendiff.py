#!/usr/bin/env python
"""Main program."""
import argparse


def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f","--format", help="set format of output")
    args = parser.parse_args()
    if args.verbosity:
        print("verbosity turned on")


if __name__ == '__main__':
    main()
