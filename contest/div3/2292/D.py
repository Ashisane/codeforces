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
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    diff = [x - y for x, y in zip(x, y)]
    acc = list(accumulate(diff))

    s1 = 0
    s2 = 0

    j = 0
    side = 0 # sunny

    for i in range(n-1, -1, -1):
        if acc[i] > 0:
            s1 = acc[i]
            side = 1
            j = i+2
            break

    while j < n:
        if diff[j] > 0:
            if side:
                s2 += diff[j]
                j+=1
            else:
                s1 += diff[j]
                j+=1
        else:
            j+=1

    print("Sunny" if s1-s2>0 else "Aubrey" if s2-s1>0 else "Draw")

def main():
    t = int(input())

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
