"강의실 배정"
import sys
# input = sys.stdin.readline

# n=int(input())
# data = []
# for _ in range(n):
#     a, b = tuple(map(int, input().split()))
#     data.append((a, b)) # 인자 2개일 경우, () 더 써줌
# data.sort(key=lambda x:x[0]) # [0]으로 오름차순 정렬 

# # print(data)
# cnt = 1
# for i in data:
#     if data[i][0] == data[i+1][0]:
#         continue
#     else:
#         cnt += 1
# print(cnt)
import heapq
n = int(input())

q = []

for i in range(n):
    a, b = map(int, input().split())
    q.append([a, b]) 
q.sort()

room = [] # heapq 에 사용해주기 위해 빈[]리슷흐 생성
heapq.heappush(room, q[0][1])

for i in range(1,n): # room에 1번째 회의끝나는 시간은 넣어주었으니, 2번째부터 계산~
    if q[i][0] < room[0]: # 현재 회의실 끝나는 시간보다 다음 회의시간이 빠르면:
        heapq.heappush(room, q[i][1]) # 새로운 회의실 개설
    else: # 현재 회의실에 이어서 회의 가능
        heapq.heappop(room) # 새로운 회의로 시간 변경을 위해 pop한 후 새로운 회의시간 push
        heapq.heappush(room, q[i][1])

print(len(room))