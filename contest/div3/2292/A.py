import sys
import os
import math
import random
import time
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right
from itertools import accumulate, permutations, combinations, pairwise

if os.path.exists("test.txt"):
    sys.stdin = open("test.txt", "r")

input = sys.stdin.readline
sys.set_int_max_str_digits(0)

R = random.getrandbits(64)

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

def solve():
    l,a,b = map(int, input().split())

    i = a%l
    sb = {0}
    while i not in sb:
        sb.add(i)
        i = (i+a)%l

    j = b%l
    bb = {0}
    while j not in bb:
        bb.add(j)
        j=(j+b)%l

    print(len(sb&bb))

def main():
    t = int(input())

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
