import sys
input=sys.stdin.readline

a=input().split('-') # []리스트로 '' 묶여 들어간다..
ans=0
# print(a)
# for i in a[0]:
#     ans += int(i)
# for j in a[1:]:
#     k = j.split('+')
#     for s in k:
#         ans -= int(s)
# print(ans)

for i in a[0].split('+'): # 얘도 + 계속해서 나올수 있으니, split 해주고
    ans += int(i)
for i in a[1:]:
    for j in i.split('+'): # 뒤에 나온 애들은 -로 split 해준 상태, +로 끊어주고
        ans -= int(j) # - 로 다 합해주기 
print(ans)