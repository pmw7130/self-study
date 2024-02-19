### ## 수 정렬하기2
# > https://www.acmicpc.net/problem/2751

import sys

n = int(input())
num = []
for i in range(n) :
    num.append(int(sys.stdin.readline()))
num.sort()
for nn in num :
    print(nn)

print(num)