# n=int(input())
s=list(map(int, input().split()))
s=sorted(s)

# print(s)
new=0
sum=0
for i in s: # 입력된 s 를 돌아야지, n을 돌면 안됨! 
    new+=i
    # i = s[i]+s[i+1]
    sum+=new
print(sum)