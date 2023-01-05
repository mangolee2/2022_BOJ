T = int(input())

for tc in (1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    last = arr[-1]
    cnt = 0
    for i in range(len(arr)-1, -1, -1):
        if last > arr[i]:
            cnt += last - arr[-1]
        else:
            last = arr[i]
        print(f'#{tc} {cnt}')
