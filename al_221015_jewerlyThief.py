""" 보석 도둑 """
# n, k = map(int, input().split())
# dia = []
# sum = 0


# for j in range(k):
#         c = int(input())

# for i in range(n):
#     m, v = list(map(int, input().split()))
#     dia.append((m,v))
#     dia.sort(key=lambda x:x[0])
#     dia.sort(key=lambda x:x[1], reverse=True) 
#     if m <= c:
#     # v = max(v)
#         sum += v
#         print(sum)

""" 우선순위 큐 """

import sys
import heapq
input = sys.stdin.readline

n,k=map(int, input().split())

dia = [list(map(int, input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]
dia.sort()
bag.sort()

result=0
temp=[]
for i in bag:
    while dia and i>=dia[0][0]:
        heapq.heappush(temp, -dia[0][1])
        heapq.heappop(dia)

    if temp:
        result += heapq.heappop(temp)

print(-result)
