## https://www.acmicpc.net/problem/11650

import sys

N = int(input())
coor = []
coor2 = []
for _ in range(N) :
    # X, Y = map(int, sys.stdin.readline().split())
    coor.append(list(map(int, sys.stdin.readline().split())))
    # coor.append([X,Y])
coor.sort()
for co in coor:
    print(f"{co[0]} {co[1]}")

print(coor)