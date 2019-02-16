#!/usr/bin/env python

import sys

def last_letter(s):
    return s[:-1].lower() + s[-1].upper()

def camel(s):
    return " ".join([last_letter(x) for x in s])
    
def main():
    for line in sys.stdin:
        tokens = line.split()
        print(camel(tokens))

if __name__ == '__main__':
    main()
