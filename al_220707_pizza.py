""" 최고의 피자 """
""" 순수하게 도우만 선택한 경우 res 에 두고 시작
1. 토핑의 열량이 높은 것부터 차례로 넣어보면서 1원당 열량의 값이 감소할 때까지 반복
감소한다면 그 전까지의 res 값 출력 """

# n = int(input()) # 토핑 종류 수
# a, b = list(map(int, input().split())) # 도우 가격, 토핑 가격
# c = int(input()) # 도우 열량

# res = int(c/a)
# for i in range(1,n+1):
#     d = list(map(int, input().split()))


""" 최고의 피자 """
import sys

read = lambda: sys.stdin.readline().rstrip()

n=int(input())
a,b=map(int, read().split())
c=int(read())
d=[]

for _ in range(n):
    d.append(int(read()))

d.sort(reverse=True)
print(d)

answer=c/a
print(answer)

for i in range(1, len(d)+1):
    calorie = c + sum(d[0:i])
    price = a + (b*i)

    if calorie/price > answer:
        answer = calorie/price
    else: 
        break
print(int(answer))