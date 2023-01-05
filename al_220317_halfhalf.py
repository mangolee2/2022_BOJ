T = int(input())

for tc in range(1, T+1):
    S = list(input())
    end = False
    for i in S:
        if S.count(i) == 2: # 문자열 S 에서 'i'가 2개 있다
            pass
        else:
            end = True
            break

    if end == True:
        print(f'#{tc} NO')
    else:
        print(f'#{tc} YES')