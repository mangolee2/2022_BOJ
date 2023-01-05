""" 수 정렬하기 보충 """
# N = int(input())
# M = []
# for i in range(N):
#     M.append(int(input()))

# # 버블 정렬
# for i in range(len(M)):
#     # print(i) 길이만큼 돈다: 0~4(5번)
#     for j in range(len(M)):
#         if M[i] < M[j]:
#             M[i], M[j] = M[j], M[i]
# for n in M:
#     print(n)


""" 분해합 """
# N = int(input())

# if N < 10:
#     print(0)
# else:
#     for i in range(N):
#         for j in str(i):
#             i -= int(j)
#     print(i)


N = int(input())
result = 0

for i in range(1, N+1):
    tmp = i + sum(map(int, str(i)))
    if tmp == N:
        result = i
        break
print(result)