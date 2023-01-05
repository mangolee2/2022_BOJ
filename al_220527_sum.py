""" 공백 없이 쓰여진 수의 합 구하기 """

t = int(input())
num = list(input())
sum = 0
for i in num:
    sum = sum + int(i)
print(sum)
