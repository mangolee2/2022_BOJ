""" 블랙잭 """
N, M = map(int, input().split())
card = list(map(int, input().split()))
tmp = 0
for i in range(N-2):
    # print(i)
    for j in range(i+1, N-1):
        # print(j)
        for k in range(j+1, N):
            # print(k)
            tmpsum = card[i] + card[j] + card[k]
            if tmp < tmpsum <= M:
                tmp = tmpsum
print(tmp)