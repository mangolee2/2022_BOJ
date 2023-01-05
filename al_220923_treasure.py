""" 보물 """

import sys
input = sys.stdin.readline

n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

# a.sort
# b.sort(reverse=True)

# sum=0
# for i in range(n):
#     ans=a[i]*b[i]
#     sum += int(ans)
# print(sum) # sum= 0 을 안하면 이런 오류가 뜸 
# # 그래서 위에 sum=0 을 명시해줌

s=0
for i in range(n):
    s += min(a) * max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))
print(s)