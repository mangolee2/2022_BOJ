import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n=int(input())
    li = [] # 필수로 담을 [] 설정

    for i in range(n):
        a, b = map(int, input().split())
        li.append((a, b))
    li.sort(key = lambda x:x[0])
    min = li[0][0]
    
    count = 1
    for i in range(1,n):
       if li[i][1] < min:
        # count += 1
        min = li[i][1]
        count += 1
    print(count)