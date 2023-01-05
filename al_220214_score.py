"""
조교의 성적 매기기
"""

# T = int(input)
# score = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

# for test_case in range(1, T+1):
#     N, K = map(int, input().split())
#     a = []
#     c = 0 
#     for t_case in range(1, N+1):
#         test = list(map(int, input().split(" ")))
#         a.append(test[0]*0.35 + test[1]*0.45 + test[2]*0.20)
#     k_score = a[K-1]
#     a.sort(reverse=True)
#     c = a.index(k_score)//(N//10)
#     print("#{} {}".format(test_case, score[c]))


"""
2번째 방법
"""
T = int(input())

for i in range(1, T+1):
    N, K = map(int, input().split())
    grade = ( "A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0" )
    scorelist = []
    for n in range(1, N+1):
        score = list(map(int, input().split()))
        score[0] = score[0]*0.35
        score[1] = score[1]*0.45
        score[2] = score[2]*0.20
        scorelist.append(sum(score))
    
    copy = scorelist.copy()
    copy.sort(reverse=True) # 정렬 후 오름차순 정리가 가능, 정렬 안하고 reverse만 할 경우 리스트의 원소 반대로만 나옴!
    # print(copy.sort(reverse=True))

    print("#{} {}".format(i, grade[int(copy.index(scorelist[K-1])/(N/10))]))