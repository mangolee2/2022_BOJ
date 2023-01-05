" 좌표 정렬하기 "
import sys
input = sys.stdin.readline

n=int(input())
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))
data.sort(key=lambda x:(x[0],x[1]) ) # 첫번째 인자 오름차순, 다음 두번째 인자 오름차순 정렬, 내림차순일 경우 - 붙음

for i in data:
    print(i[0],i[1])