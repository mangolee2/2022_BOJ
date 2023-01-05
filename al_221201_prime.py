" 소인수분해 "

# n= int(input())

# if n==1:
#     print('')
# for i in range(2, n+1):
#     # print(i)
#     if n%i == 0:
#         # print(n%i)
#         while n%i ==0:
#             print(i)
#             n = n/i

" 소수 구하기 "
# n=int(input()) # 3
# m=int(input()) # 16

def prime(n):
    if n==1:
        pass
    else:
        for i in range(2, int(n**0.5)+1): # 입력숫자의 제곱근까지만 확인하여도 소수판별가능?
            if n%i == 0: # 이면 나누어떨어지면 소수가 아니다~ 
                return False
        return True

n,m = map(int, input().split())
for i in range(n, m+1):
    if prime(i): # True 이면
        print(i)
