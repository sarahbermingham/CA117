#!/usr/bin/env python

import sys

def diamond(n):
    width = n-2
    for i in range(1, n):
        print(width * " " + i * " *")
        width -= 1

    print("*" + (n-1) * " *")
    width = 0

    for i in range(n-1, 0, -1):
        print(width * " " + i * " *")
        width += 1

def main():
    size = int(sys.argv[1])
    diamond(size)

if __name__ == '__main__':
    main()