""" A->B """
A,B=map(int, input().split())

cnt=1
while A != B: # 2 162
    tmp = B
    if B%10 == 1:
        B= B//10
        cnt+=1
    elif B%2 == 0:
        B= B//2
        cnt+=1
    print(tmp)
    # print(B)
    # if tmp == B:
    #     cnt = -1
    #     print(tmp)
    #     break
    if tmp == B:
        cnt = -1
        break
print(cnt)
