""" 숫자 카드 게임 """

""" 
n, m = list(map(int, input().split()))
data=[]

result=0
for i in range(n):
    data = list(map(int, input().split()))

    mini = min(data)
    result = max(result, mini)
print(result)
"""

""" 1이 될 때까지 """
 
n, m = map(int, input().split())
cnt = 0
while n >= m:
    while (n%m) != 0:
        n-=1
        cnt+=1
    n//=m
    cnt += 1

while n>1:
    n -= 1
    cnt += 1

print(cnt)