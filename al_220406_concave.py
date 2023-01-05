# T = int(input())
# o = []
# # . = []

# for i in range(1, T+1):
#     N = int(input())
#     for j in range(1, N+1):
#         if j == o:
#                 print(f'{k} "YES"')
            
#         for k in j:
#             if k == o:
#                 print(f'{k} "YES"')
            

def A(arr):
    dr = [0, 1, 1, 1]
    dc = [1, 0, 1, -1]
    for start_r in range(N):
        for start_c in range(N):
            if arr[start_r][start_c] == 'o':
                for d in range(4):
                    r = start_r
                    c = start_c
                    cnt = 0
                    while 0 <= r <= N-1 and 0 <= c <= N-1 and arr[r][c] == 'o':
                        cnt += 1
                        r += dr[d]
                        c += dr[d]
                        if cnt >= 5:
                            return 'YES'
    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    print(f'#{tc} {A(arr)}')