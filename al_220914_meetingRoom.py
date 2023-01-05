""" 회의실 배정 """

# N=int(input())
# time=list()
# for i in range(N):
#     time.append(input().split())

#     if time[1]-time[0]

n = int(input())
s = []
for i in range(n):
    first, second = map(int, input().split())
    s.append([first, second])
s = sorted(s, key=lambda a:a[0]) # 시작 시간을 기준으로 오름차순
s = sorted(s, key=lambda a:a[1]) # 끝나는 시간을 기준으로 오름차순
# print(s, key)
last = 0 # 회의의 마지막 시간을 저장하는 변수
cnt = 0 # 회의 개수를 저장하는 변수
for i,j in s:
    # print(i, j)
    if i >= last: # 시작 시간이 회의의 마지막 시간보다 크거나 같을 경우 
        cnt += 1
        last = j
print(cnt) 


""" or """
import sys
n = int(sys.stdin.readline())
time =[[0]*2 for _ in range(n)]

for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    time[i][0] = s
    time[i][1] = e
time.sort(key = lambda x : (x[1], x[0]))

cnt = 1
end_time = time[0][1]
for i in range(1, n):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]
print(cnt)