import sys

N = int(input())
test = []
for i in range(N) :
    age, name = (map(str , sys.stdin.readline().split()))
    test.append([int(age), name, i])

test.sort(key=lambda x:(x[0], x[2]))

for age, name, idx in test :
    print(f"{age} {name}")