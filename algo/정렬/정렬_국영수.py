import sys

N = int(input())
arr = []
for i in range(N) :
    name, kor, eng, math = map(str, sys.stdin.readline().split())
    arr.append([name, int(kor), int(eng), int(math)])

arr.sort(key= lambda x : (-x[1], x[2], -x[3], x[0] ))

for name, kor, eng, math in arr :
    print(name)
