""" 피보나치 함수 소스 코드 """
# fib(1) = 1, fib(2) = 1, fib(3) = 2, fib(4) = 3
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)

# print(fib(4))
# print(fib(5))
# print(fib(6))


""" 피보나치 수열 소스 코드 """
# d = [0] * 100

# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     if d[x] != 0:
#         return d[x]
#     if d[x] != 0:
#         return d[x]
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]

# print(fibo(99))

""" 1로 만들기 """
x = int(input())

d = [0] * 30001

for i in range(2, x + 1):
    d[i] = d[i-1] + 1 # 현재의 수에서 1을 빼는 경우

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1) # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 3 == 0: 
        d[i] = min(d[i], d[i//3] + 1) # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 5 == 0: 
        d[i] = min(d[i], d[i//5] + 1) # 현재의 수가 5로 나누어 떨어지는 경우 

print(d[i]) 

