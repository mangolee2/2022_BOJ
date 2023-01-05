import sys
input = sys.stdin.readline

n=int(input())

data= 10001 * [0] # 메모리문제해결
for i in range(n):
    data[int(input())] += 1

for i in range(10001):
    if data[i] != 0:
        for j in range(data[i]):
            print(i)