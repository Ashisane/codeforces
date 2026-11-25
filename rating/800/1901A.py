import sys

input = sys.stdin.readline

def solve():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    diff = [arr[i]-arr[i+1] for i in range(n-1)]
    diff.append(0-arr[0])
    diff.append((arr[-1]-x)*2)

    print(-1*min(diff))

def main():
    t = int(input())

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
