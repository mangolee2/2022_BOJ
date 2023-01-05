""" 뒤집기 """

s = input()

cnt = 0

for i in range(len(s)):
    if s[i] != s[i-1]:
        cnt += 1

print(len(s))
print(cnt//2)

