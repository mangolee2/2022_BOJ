""" 금민수 구하기 """

# n=int(input())

# while True:
#     flag=True
#     for i in str(n):
#         if i !='4' or i !='7':
#             flag=False
#             n-=1
#     if flag:
#         print(n)
#         break

""" 금민수 2 """
import sys

n=int(sys.stdin.readline().rstrip())

for i in range(n):
    num=n-i
    # print(num)
    check=0
    for j in str(num):
        if j=='7' or j=='4':
            pass
        else:
            check=1
            break
    if check==0:
        break
print(num)