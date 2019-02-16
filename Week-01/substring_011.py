#!/usr/bin/env python

import sys

def sub(chars, s):
    if chars in s:
        return True
    else:
        return False

def main():
    for line in sys.stdin:
        [chars, s] = line.lower().strip().split()
        print(sub(chars, s))

if __name__ == '__main__':
    main()
