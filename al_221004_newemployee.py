""" 신입사원 """

import sys
input=sys.stdin.readline

n=int(input())

for i in range(n):
    m=int(input()) # 1 <= n <= 100,000
    data=[]

    for j in range(m):
        a, b = map(int, input().split())
        data.append((a,b))
    data.sort(key = lambda x: x[0])
    min = data[0][1]

    count=1
    for i in range(1,m):
        if data[i][1] < min:
            count += 1
            min = data[i][1]
            # count += 1
    print(count)