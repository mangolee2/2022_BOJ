# T = int(input())

# Ci = input().upper
# Ki = int(input())

# compression = {Ci, Ki}
# original = {Ci*Ki}


# for i in range(1, T+1):
#     compression = list(map((Ci, Ci.split())), Ki)
 
#     print(f'#{i} {original}')
    

"""
간단한 압축풀기
"""
for tc in range(1, int(input())+1):
    N = int(input())
    lis = []
    words = ''
    for i in range(N):
        lis.append(input().split())
    for i in range(N):
        words += lis[i][0]*int(lis[i][1])
        # print(words)
    print('#{}'.format(tc))
    cnt = 0
    for w in words:
        print(w, end='')
        cnt += 1
        if cnt == 10:
            print()
            cnt = 0
    print()