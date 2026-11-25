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

    arr = [e[0]]

    for i in range(n-1):
        if e[i] <= e[i+1]:
            arr.append(e[i+1])
        if e[i+1] < e[i]:
            arr.append(e[i+1])
            arr.append(e[i+1])

    r = " ".join(map(str, arr))
    print(len(arr))
    print(r)

def main():
    t = int(input())

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
