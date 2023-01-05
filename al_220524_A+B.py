""" A, B 입력받은 후 A+B 출력 """
T = int(input())
for i in range(1, T+1):
    num = list(map(int, input().split()))
    # for j in num:
    print(num[0] + num[1])

