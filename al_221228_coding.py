" 배수와 약수 "
# while True:
#     n,m=list(map(int, input().split()))
#     # a=[n,m]
#     # a.sort()
#     if n==0 and m==0:
#         break
#     if n>m and n%m==0:
#         print('multiple')
#     elif n<m and m%n==0:
#         print("factor")
#     else:
#         print("neither")
" 배수 "
# t=int(input())

# data=list(map(int,input().split())) # 4 2
# data.sort()
# if len(data)<2:
#     ans = data[0]*data[0]
#     print(ans)
# else:
#     ans = data[0]*data[-1]
#     print(ans)

" 최대공약수와 최소공배수 "
# n,m=map(int,input().split())
# ans=[]
# ans2=[]
# while True:
#     if n%2==0 and m%2==0:
#         n=n//2
#         m=m//2
#         # print(n,m)
#         ans.append(2)
#         # print(ans)
#     elif n%3==0 and m%3==0:
#         n=n//3
#         m=m//3
#         # print(n,m)
#         ans.append(3)
#         # print(ans)
#     else:
#         ans2=n,m 
#         # print(ans2)
#         break 
# total=1
# for i in ans:
#     total *= i
# print(total)
# for i in ans2:
#     total *= i 
# print(total)

# 유클리드 호제법
# import sys

# A,B=map(int, sys.stdin.readline().split())
# a,b=A,B # 원데이터 놔두기 위해

# while b != 0:
#     a = a%b # a 최대공약수
#     a,b= b,a 
# print(a)
# print(A*B//a)

" 최소공배수 "
import sys
input=sys.stdin.readline

t=int(input())
for i in range(t):
    N,M=map(int, input().split())
    n,m=N,M
    gcd = [n,m]
    gcd.sort() # 내림차순
    while m != 0:
        n = n%m
        n,m = m, n
    print(N*M//n)


