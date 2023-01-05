""" 수 정렬하기 """

N = int(input())
M = []
for i in range(N):
    M.append(int(input()))

M = sorted(M)
for i in range(len(M)):
    print(M[i])

""" set과 add """
N = int(input())
M = set()
for i in range(N):
    M.add(int(input()))
M = list(M)
M.sort()
for i in range(len(M)):
    print(M[i])


""" 버블정렬로 정렬하기 """
N = int(input())
M = []
for i in range(N):
    M.append(int(input()))

# 버블 정렬
for i in range(len(M)):
    for j in range(len(M)):
        if M[i] < M[j]:
            M[i], M[j] = M[j], M[i]
for n in M:
    print(n)

""" 삽입정렬로 정렬하기 """
N = int(input())
M = []
for i in range(N):
    M.append(int(input()))

# 삽입 정렬
for i in range(len(M)):
    while (i>0) & (M[i] < M[i-1]):
        M[i], M[i-1] = M[i-1], M[i]

        i -= 1
for i in M:
    print(n)
    
