""" 별 찍기 7 & 9 """

# n = int(input())
# for i in range(2*n):
#     print((n-i)*" ", end="")
#     print((2*i-1)*'*')

# n = int(input())
# for i in range(n): # i 가 1 부터 시작함
#     print(" "*i + "*"*(2*(n-i-1)+1))
# for i in range(1, n):
#     print(" "*(n-i-1) + "*"*(2*i+1)) # i 는 0 부터 시작함

""" 한 포문으로 별 찍기 """
n = int(input())
star = 1
for i in range(2*n):
    if i < 2*n-1 :
        print(" "*(n-i) + "*"*star)
        star += 2
    elif star == 2*n-1:
        print(" "*(n-i) + "*"*star)
        star -= 2
    else:
        print(" "*(n-i) + "*"*star)
        star -= 2