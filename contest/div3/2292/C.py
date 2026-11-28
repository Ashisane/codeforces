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
    n = int(input())
    s = input().strip()
    clouds=[*s]

    if n % 2 != 0:
        print("NO")
    elif n == 2:
        print("YES" if s[0] == s[1] else "NO")
    else:
        print("NO" if all(s[i] != s[i + 1] for i in range(n - 1)) else "YES")

def main():
    t = int(input())

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
