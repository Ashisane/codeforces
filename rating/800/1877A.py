import sys

input = sys.stdin.readline


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

def solve():
    n = int(input())
    e = list(map(int, input().split()))

    print(sum(e)*-1)

def main():
    t = int(input())

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
