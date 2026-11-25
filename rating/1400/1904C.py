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
    n, k = map(int, input().split())
    arr = sorted(map(int, input().split()))

    if k >= 3:
        print(0)
        return

    ans = arr[0]
    for i in range(n - 1):
        ans = min(ans, arr[i + 1] - arr[i])

    if k == 1:
        print(ans)
        return

    for i in range(n - 1):
        for j in range(i + 1, n):
            diff = arr[j] - arr[i]
            idx = bisect_left(arr, diff)

            if idx < n:
                ans = min(ans, arr[idx] - diff)
            if idx > 0:
                ans = min(ans, diff - arr[idx - 1])

            if ans == 0:
                print(0)
                return

    print(ans)

def main():
    t = int(input())

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
