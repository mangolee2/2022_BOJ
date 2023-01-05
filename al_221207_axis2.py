" 좌표 정렬하기 2 "

import sys
input = sys.stdin.readline

n=int(input())
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))
data.sort(key=lambda x:(x[1],x[0]) )

for i in data:
    print(i[0],i[1])