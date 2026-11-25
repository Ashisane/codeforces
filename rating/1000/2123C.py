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

R = random.getrandbits(64)

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

def solve():
    n = int(input())
    e = list(map(int, input().split()))

    a = list(accumulate(e, min))
    b = list(accumulate(e[::-1], max))[::-1]

    r = ["1" if e[i] == a[i] or e[i] == b[i] else "0" for i in range(n)]

    print("".join(r))

def main():
    t = int(input())

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
