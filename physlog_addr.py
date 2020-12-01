#!/usr/bin/env python

def main(args):
    output = ""
    output += args[1] + ":"
    base = int(args[2])
    laddr = int(args[3])
    length = int(args[4])
    paddr = base + laddr

    if (laddr>length):
        output+=str(laddr) + ">" + str(length) + ", invalid"
        print(output)
        return
    else:
        output+= str(base) +"+"+ str(laddr) + "=" + str(paddr) + "," + str(laddr) + "<" + str(length) + ", valid"
        print(output)
    pass


if __name__ == '__main__':
    import sys
    main(sys.argv)
