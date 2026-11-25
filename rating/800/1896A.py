import sys

input = sys.stdin.readline

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    c = True

    while c:
        c = False
        for i in range(1, n-1):
            if(arr[i-1]<arr[i]>arr[i+1]):
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp

                c = True

    print("yes" if is_sorted(arr) else "no")

def main():
    t = int(input())

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
