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
    n = int(input())
    arr = list(map(int, input().split()))


def main():
    t = int(input())

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
