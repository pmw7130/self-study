import sys

N = int(input())
coor = []
coor2 = []
for i in range(N) :
    coor.append(list(map(int, sys.stdin.readline().split())))
    coor2.append([coor[i][1], coor[i][0]])

coor2.sort()
for x,y in coor2 :
    print(y, x)
