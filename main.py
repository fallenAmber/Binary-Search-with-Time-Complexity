
import random
import math
import time

def naive_search(l, target):

    for i in range(len(l)):

        if l[i]==target:
            return f"{target} is in the list"

    return -1

def BinarySearch(l, target, low=None, high=None):

    if low is None:
        low =0
    if high is None:
        high = len(l)-1

    midpoint = (high+low)//2

    if target==l[midpoint]:
        return midpoint

    elif  target < l[midpoint]:
        return BinarySearch(l, target, low, midpoint-1)
    elif target > l[midpoint]:
        return BinarySearch(l, target, midpoint+1, high)


if __name__ == '__main__':
    length = 10000
    sorted_list = set()

    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start), "seconds")

    start = time.time()
    for target in sorted_list:
        BinarySearch(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start), "seconds")

