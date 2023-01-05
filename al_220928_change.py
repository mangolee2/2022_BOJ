""" 잔돈 """

li=[500, 100, 50, 10, 5, 1]
n=int(input())
a=1000-n # 잔돈 
ans=0
for i in li:
    ans+=a//i
    a=a%i
print(ans)
