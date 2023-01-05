""" 카드 정렬 """
# import sys
# input = sys.stdin.readline

# n=int(input())
# data=[]
# for _ in range(n):
#     data.append(int(input()))

# data.sort()
# # print(data)

# sum=0
# # data[i+1]
# for i in data:
#     data[i+1] = data[i] + data[i+1] 
#     sum += data[i+1]
# print(data[i+1])

import heapq
q=[]
n=int(input())

for i in range(n):
    heapq.heappush(q, int(input()))

sum = 0
while len(q) > 1:
    temp1 = heapq.heappop(q) # 최소값이 나오게 됨
    temp2 = heapq.heappop(q) # 그 다음 최소값
    heapq.heappush(q, (temp1+temp2)) # 두 최소값의 합 넣어주고
    sum += temp1 + temp2
print(sum)