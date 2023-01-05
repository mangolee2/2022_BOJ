""" 영수증 """

# total=int(input()) # 250000
# n=int(input())
# li=[]
# sum=0
# for i in range(n):
#     li.append(input().split(' '))
# for j in li:
#     sum += li[j][0]*li[j][1]
#     if n == sum:
#         print('Yes')
#     else:
#         print("No")

    
total = int(input())
n=int(input())
# total_price= 0
for i in range(n):
    amount, units = map(int, input().split())
    total -= amount*units
if total == 0:
        print('Yes')
else:
        print('No')