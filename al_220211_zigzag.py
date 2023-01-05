"""
지그재그 숫자
"""

# t = int(input())

# for num in range(1, t+1):
#     num = list(map(int, input()))
#     if num % 2 : # 홀수일 경우, 1 -> True 로 인식
#         print(sum(num))
#     else: 
#         # num = - * (num)
#         print(sum(num))

T = int(input())

for t in range(1, T+1):
    N = int(input())
    sum = 1
    for i in range(2, N+1):
        if i%2 == 0:
            sum -= i
        else:
            sum += i
    print("#{} {}".format(t, sum))