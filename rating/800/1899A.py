import sys

input = sys.stdin.readline

def solve():
    n = int(input())

    if((n-1)%3==0 or (n+1)%3==0):
        print("First")
    else:
        print("Second")

def main():
    t = int(input())

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
