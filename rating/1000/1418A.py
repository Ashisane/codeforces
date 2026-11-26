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
    x, y, k = map(int, input().split())

    # 1 + n(x-1) = y*k + k
    print(-(-(y*k+k-1)//(x-1))+k)

def main():
    t = int(input())

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
