# def solution(n):
#     n = int(input())

#     new = str(n)
#     add = 0
#     for i in range(len(new)):
#         add += int(new[i])
#         return add  

# print(solution(6789))
"""
자릿수 더하기
"""

T = int(input())
new = str(T)
# for i in range(len(new)):
print(sum(map(int, new)))