#!/usr/bin/env python

def main(args):
    p = int(args[1])
    first = True
    second = True
    for a in args:
        if (first):
            first=False
        else:
            if (second):
                second=False
            else:
                v = int(a)
                i = int(v /p)
                r = v % p
                print("Page " + str(i) + ", offset" + str(r))


if __name__ == '__main__':
    import sys
    main(sys.argv)
