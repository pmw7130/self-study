import sys

N = int(input())
arr = [0 for _ in range(N)]
for i in range(N) :
    # arr.append(int(sys.stdin.readline()))
    arr[i] = int(sys.stdin.readline())

arr.sort()
for j in arr :
    print(j)