#!/usr/bin/env python

import sys

def caps(a):
    s = ""
    for token in a:
        word = token.strip().capitalize()
        if s == "":
            s = word
        else:
            s = s + " " + word
    return s

def main():
    for line in sys.stdin:
        tokens = line.strip().split()
        print(caps(tokens))

if __name__ == '__main__':
    main()
