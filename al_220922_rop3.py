""" 로프rope """

n=int(input())
rope=[]
ans=[]
for i in range(n): # (1,n) 으로 범위지정할 경우, n이 2일경우, 1 밖에 안되니 2출력 안됨
    rope.append(int(input())) # 세로로 입력값 입력시는 .append 사용 (not list(map))
rope.sort(reverse=True) # rope=rope.sort 는 안됨
# for j in rope:
# ans=rope[0]*n
for j in range(n):
    ans.append(rope[j]*(j+1))

print(max(ans))