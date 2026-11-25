import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    e = list(map(abs, map(int, input().split())))

    print(min(e))

if __name__ == "__main__":
    solve()
