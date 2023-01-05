""" 홀수값 더하기 """
T = int(input())

for test_case in range(1, T + 1):
    y = list(map(int, input().split()))
    result = 0
    for i in y:
        if i % 2: # 1을 true 로 인식
            result += i
    print(f"#{test_case}", result)

