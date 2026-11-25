import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    arr = input()

    i = 0
    counter = 0

    while i < n:
        if arr[i] == ".":
            t = 1
            for j in range(i+1, n):
                if arr[j] == ".":
                    if arr[j+1] == ".":
                        counter = 2
                        i = n
                        break
                    t = 2
                    i += 1
                else:
                    i += 1
                    break
            if i < n:
                i += 1
                counter += t
        else:
            i += 1

    print(counter)

def main():
    t = int(input())

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
