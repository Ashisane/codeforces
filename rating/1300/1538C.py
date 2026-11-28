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

def count_less(arr, x, n):
    t = 0
    a = 0
    b = n-1

    while a < b:
        if (arr[a] + arr[b] <= x):
            t += b-a
            a += 1
        else:
            b -= 1

    return t

def solve():
    n, l, r = map(int, input().split())
    arr = sorted(map(int, input().split()))

    print(count_less(arr, r, n)-count_less(arr, l-1, n))

def main():
    t = int(input())

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
