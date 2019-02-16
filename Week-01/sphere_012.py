#!/usr/bin/env python

import sys
import math

def radius(r, s, t):
   print("Radius (m)      Area (m^2)    Volume (m^3)")
   print("----------      ----------    ------------")
   while r <= t:
      volume = (4 / 3) * math.pi * r ** 3
      area = 4 * math.pi * r ** 2
      print(('{:10.1f}'.format(r)), " " * 4, ('{:10.2f}'.format(area)), " " * 4, ('{:10.2f}'.format(volume)))

      r += s

def main():
   return radius(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))

if __name__ == "__main__":
   main()
