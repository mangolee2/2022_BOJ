""" 기타줄 """
import sys
input = sys.stdin.readline

n,m=map(int, input().split())

price_li = []
ans = 0
for _ in range(m):
    price= tuple(map(int, input().split()))
    price_li.append(price)
    
pack_li = sorted(price_li, key=lambda x:x[0])
sin_li = sorted(price_li, key=lambda x:x[1])

if pack_li[0][0] <= sin_li[0][1]*6:
    ans = pack_li[0][0] * (n//6) + sin_li[0][1]*(n%6)
    if pack_li[0][0] < sin_li[0][1] * (n%6):
        ans = pack_li[0][0] * ((n//6)+1)
else:
    ans = sin_li[0][1] * n 
print(ans)