#!/usr/bin/env python

import sys

def main():
    rows = []
    clubs = []

    for line in sys.stdin:
        rows.append(line.rstrip('\n'))

    for i in range(len(rows)):
        rows[i] = rows[i].split()
        club = " ".join(rows[i][1:-8])
        rows[i][1] = club
        del rows[i][2:-8]
        clubs.append(club)

    club_width = len(max(clubs, key = len))

    print("{:>3} {:<{}} {:>2} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3}".format("POS", "CLUB", club_width, "P", "W", "D", "L", "GF", "GA", "GD", "PTS"))

    for i in rows:
        sys.stdout.write('{:>3} {:<{}} {:>2}'.format(i[0], i[1], club_width, i[2]))
        for j in range(3, len(i)):
            sys.stdout.write('{:>4}'.format(i[j]))
        sys.stdout.write('\n')

if __name__ == '__main__':
    main()
