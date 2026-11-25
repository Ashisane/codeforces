import sys
from collections import Counter

input = sys.stdin.readline

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

def solve():
    n = int(input())
    arr = list(Counter(map(int, input().split())).items())

    l = len(arr)

    c = False

    if l > 2:
        c = False
    elif l <= 1:
        c = True
    else:
        x = arr[0][1]
        y = arr[1][1]
        if(x==y or x==y+1 or x+1==y):
            c = True

    print("yes" if c else "no")

def main():
    t = int(input())

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
