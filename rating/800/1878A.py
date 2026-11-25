import sys
import os
import math
import random
import time
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right
from itertools import accumulate, permutations, combinations, pairwise

input = sys.stdin.readline

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

def solve():
    n, m = map(int, (input().split()))
    a = list(map(int, input().split()))

    print("yes" if m in a else "no")

def main():
    t = int(input())

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
