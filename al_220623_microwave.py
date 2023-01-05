# t = int(input())
# A = 300
# B = 60
# C = 10

# for A in range(1, t+1):
#     a = t//A
#     t1 = t%A
#     continue
# for B in range(1, t1+1):
#     b = t1//B
#     t2 = t1%B
#     continue
# for C in range(1, t2+1):
#     c = t2//C
#     t3 = t2%C
#         # print(c, t3)
# print(a, b, c)
 
# else:
#     print('-1')


""" 전자레인지 """
T = int(input())
if (T%10) != 0:
    print('-1')
else:
    A = B = C = 0
    A = T // 300
    B = (T % 300) // 60
    C = ((T % 300) % 60)// 10
    print(A, B, C)