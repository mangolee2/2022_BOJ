""" 덩치 """
N = int(input())
people = []
for i in range(N):
    w, h = map(int, input().split())
    people.append((w, h))

for j in people:
    rank = 1
    for k in people: # [0] 몸뭄게 비교, [1] 키 비교
        if (j[0]!=k[0]) & (j[1]!=k[1]): # 자신을 제외하고 비교
            if (j[0]<k[0]) & (j[1]<k[1]):
                rank += 1
    print(rank)