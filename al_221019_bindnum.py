""" 수 묶기 """
n=int(input())

pos = []
neg = []

sum = 0
for i in range(n):
    num = int(input())
    
    if num > 1:
        pos.append(num)
    elif num <= 0:
        neg.append(i)
    else:
        sum += num 
# 정렬
pos.sort(reverse=True)
neg.sort()
# 양/음수 2개 묶기
for i in range(0, len(pos), 2):
    if i+1 >= len(pos):
        sum += pos[i]
    else:
        sum += (pos[i]*pos[i+1])

for i in range(0, len(neg), 2):
    if i+1 >= len(neg):
        sum += neg[i]
    else:
        sum += (neg[i]*neg[i+1])

print(sum)
