T = int(input())

for test_case in range(1, T+1):
    numbers = list(map(int, input().split()))
    result = 0
    number = [1, 3, 5, 7, 8, 10, 12]
    if numbers[0] != numbers[2]:
        if numbers[0] in number:
            result += (32 - numbers[1]) + numbers[3]
        elif numbers[0] == 2:
            result += (29 - numbers[1]) + numbers[3]
        else:
            result += (31 - numbers[1]) + numbers[3]
        for i in range(numbers[0] + 1, numbers[2]):
            if i in number:
                result += 31
            elif i == 2:
                result += 28
            else:
                result += 30
        print(f'#{test_case} {result}')

    else:
        result = numbers[3] - numbers[1] + 1
        print(f'#{test_case} {result}')