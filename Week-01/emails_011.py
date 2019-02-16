#!/usr/bin/env python

import sys

def emails(s):
    nums = "0123456789"
    tokens = s.split("@")
    [first, last] = tokens[0].strip(nums).split(".")
    name = first.capitalize() + " " + last.capitalize()
    return name

def main():
    for l in sys.stdin:
        tokens = l.strip()
        print(emails(tokens))

if __name__ == '__main__':
    main()
