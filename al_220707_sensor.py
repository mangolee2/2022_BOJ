""" 최고의 피자 """
import sys

read = lambda: sys.stdin.readline().rstrip()

n=int(input())
a,b=map(int, read().split())
c=int(read())
d=[]

for _ in range(n):
    d.append(int(read()))

d.sort(reverse = True)
answer = c/a

for i in range(1, len(d)+1):
    cal = c + sum(d[0:i])
    price = a + (b*i)

    if cal/price > answer:
        answer = cal/price
    else:
        break
print(int(answer))