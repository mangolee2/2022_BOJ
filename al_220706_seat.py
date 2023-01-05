""" 누울 자리를 찾아라 """

n=int(input())
li=[]
r,c=0,0
cnt=0
for i in range(n):
    li.append(list(input()))
for i in range(n):
    cnt=0
    for j in range(n):
        if li[i][j]=='.':
            cnt+=1
        else:
            cnt=0
        # 가로로 누울자리 체크
        if cnt == 2:
            # .. 2 일 경우, 행 갯수 1 추가해주기
            r += 1

# 세로로 누울자리 체크
for i in range(n):
        cnt=0
        for j in range(n):
            # 세로로 . 체크할 때, li[j][i] i와 j의 순만 바꾸어줌
            if li[j][i] == '.':
                cnt+=1
            else:
                cnt=0
            if cnt==2:
                c += 1
print(r,c)
