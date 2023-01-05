"""
달팽이 숫자
"""
T = int(input())

for i in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    num = 1  # 숫자
    row = 0  # x좌표
    col = -1 # y좌표
    trans = 1 # 진행방향 설정
    while N > 0:
        for _ in range(N):
            col += trans
            arr[row][col] = num
            num += 1
        N -= 1
        for _ in range(N):
            row += trans
            arr[row][col] = num
            num += 1
        trans *= -1

    print("#{}".format(i))
    for i in range(len(arr)):
        print(*arr[i]) 