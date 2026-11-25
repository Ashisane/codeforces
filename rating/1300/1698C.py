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

def tsum(arr):
    t = []
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                t.append(arr[i]+arr[j]+arr[k])
    return t

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    pos = 0
    neg = 0
    zeros = 0
    _arr = []

    for x in arr:
        if x > 0:
            pos += 1
            if pos > 2:
                print("NO")
                return
            _arr.append(x)
        elif x < 0:
            neg += 1
            if neg > 2:
                print("NO")
                return
            _arr.append(x)
        else:
            if zeros < 2:
                zeros += 1
                _arr.append(0)

    m = len(_arr)
    for i in range(m - 2):
        for j in range(i + 1, m - 1):
            for k in range(j + 1, m):
                if _arr[i] + _arr[j] + _arr[k] not in _arr:
                    print("NO")
                    return

    print("YES")

def main():
    t = int(input())

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
