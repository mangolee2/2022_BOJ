string = input()
s=string.split(' ')# 띄어쓰기로 저장

# print(s)
li0=[]
check=[]
for i in s:
    li0.append(i[0])
    if i[0].isupper():
        check.append(i[0])
ans=''.join(check)
if ans == 'UCPC':
    print('I love UCPC')
else:
    print('I hate UCPC')