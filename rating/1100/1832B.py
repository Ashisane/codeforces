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

    e = list(accumulate(sorted(map(int, input().split())), initial=0))
    s = 0

    for i in range(k+1):
        #print(e[-1-i])
        #print(e[2*(k-i)])

        t = e[-1-i] - e[2*(k-i)]

        s = max(t,s)

    print(s)

def main():
    t = int(input())

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
