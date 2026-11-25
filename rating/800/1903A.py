import sys
from itertools import pairwise

input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    print("YES" if k > 1 or all(a <= b for a, b in pairwise(arr)) else "NO")

def main():
    t = int(input())

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
