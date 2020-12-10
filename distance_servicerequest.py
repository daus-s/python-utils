#!/usr/bin/env python

def inv_sort(ints):
    ints = sort(ints)
    resultant = []
    l = len(ints)-1
    for i in range(len(ints)):
        resultant.append(ints[l-i])
    return resultant

def sort(ints):
    l = len(ints)
    resultant = []
    for i in range(l):
        current_min = ints[0]
        for j in range(len(ints)):
            if ints[j] < current_min:
                current_min = ints[j]
        resultant.append(current_min)
        ints.remove(current_min)

    return resultant

def fcfs(ints, init):
    d = 0
    prev = init
    for i in range(len(ints)):
        d += abs(ints[i] - prev)
        prev = ints[i]
    return d

def min_index(ints):
    mindex = 0
    mvalue = ints[0]
    for i in range(len(ints)):
        if ints[i] < mvalue:
            mvalue = ints[i]
            mindex = i
    return mindex

def diff_arr_fun(ints, current):
    diff_arr = []
    for i in range(len(ints)):
        diff_arr.append(abs(ints[i]-current))
    return diff_arr

def sstf(ints, init):
    l = len(ints)
    copy_ints = []
    for i in range(l):
        copy_ints.append(ints[i])
    d = 0
    prev = init
    current = ints[0]
    for i in range(l-1):
        diff_arr = diff_arr_fun(ints, current)
        index = min_index(diff_arr)
        d += abs(ints[index] - prev)
        del ints[index]
        prev = current
        current = ints[index]

    ints = copy_ints
    return d

def scan(ints, init):
    d = 0
    ints_less = []
    ints_more = []
    for i in range(len(ints)):
        if ints[i] <= init:
            ints_less.append(ints[i])
        elif ints[i] >= init:
            ints_more.append(ints[i])
    ints_less = inv_sort(ints_less)
    ints_more = sort(ints_more)

    ints = ints_more + ints_less
    prev = init
    for i in range(len(ints)):
        d += abs(ints[i] - prev)
        prev = ints[i]
    return d

def cscan(ints, init):
    d = 0
    ints_less = []
    ints_more = []
    for i in range(len(ints)):
        if ints[i] <= init:
            ints_less.append(ints[i])
        elif ints[i] >= init:
            ints_more.append(ints[i])
    ints_less = sort(ints_less)
    ints_more = sort(ints_more)

    prev = init
    for i in range(len(ints_more)):
        d += abs(ints_more[i] - prev)
        prev = ints[i]
    d += (4999-prev) + 4999
    prev = 0;
    for i in range(len(ints_less)):
        d += abs(ints_less[i] - prev)
        prev = ints[i]
    return d


def look(ints, init):
    d = 0
    ints_less = []
    ints_more = []
    for i in range(len(ints)):
        if ints[i] <= init:
            ints_less.append(ints[i])
        elif ints[i] >= init:
            ints_more.append(ints[i])
    ints_less = sort(ints_less)
    ints_more = sort(ints_more)

    prev = init
    for i in range(len(ints_more)):
        d += abs(ints_more[i] - prev)
        prev = ints[i]
    d += prev-ints_less[0]
    prev = ints_less[0]
    for i in range(len(ints_less)):
        d += abs(ints_less[i] - prev)
        prev = ints[i]
    return d





def main(args):
    arr = args[1].split(",")
    ints = []
    for i in range(len(arr)):
        ints.append(int(arr[i]))
    print("distance travelled for FCFS is: " + str(fcfs(ints, int(args[2]))))
    print("distance travelled for SSTF is: " + str(sstf(ints, int(args[2]))))
    ints = []
    for i in range(len(arr)):
        ints.append(int(arr[i]))
    print("distance travelled for SCAN is: " + str(scan(ints, int(args[2]))))
    print("distance travelled for LOOK is: " + str(look(ints, int(args[2]))))
    print("distance travelled for CSCAN is: " + str(cscan(ints, int(args[2]))))


if __name__ == '__main__':
    import sys
    main(sys.argv)
