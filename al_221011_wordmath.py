# import sys

# input = sys.stdin.readline

# n= int(input())

# alphabet_dict = {'A':0, 'B':0 ,'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
# alphabet_list = []
# answer = 0
# pocket = []

# for _ in range(n):
#     alphabet = input()
#     pocket.append(alphabet)

# for alphabet in pocket:
#     for i in range(len(alphabet)):
#         num = 10**(len(alphabet) - i - 1)
#         alphabet_dict[alphabet[i]] += num

# for value in alphabet_dict.values():
#     if value > 0:
#         alphabet_list.append(value)

# sorted_list = sorted(alphabet_list, reverse=True)
# for i in range(len(sorted_list)):
#     answer += sorted_list[i] * (9-i)

# print(answer)


import sys

n = int(sys.stdin.readline())

alpha = [] # 단어를 저장할 리스트
alpha_dict = {} # 단어 내의 알파벳별로 수를 저장할 딕셔너리
numList = [] # 수를 저장할 리스트

for i in range(n): # 단어를 입력받음
    alpha.append(sys.stdin.readline().rstrip())

for i in range(n): # 모든 단어에 대해서
    for j in range(len(alpha[i])): # 단어의 길이만큼 실행
        if alpha[i][j] in alpha_dict: # 단어의 알파벳이 이미 dict에 있으면
            alpha_dict[alpha[i][j]] += 10 ** (len(alpha[i])-j-1) # 자리에 맞게 추가 ( 1의 자리면 1 )
        else:   # 자리에 없으면 새로 추가 ( 10의 자리면 10 )
            alpha_dict[alpha[i][j]] = 10 ** (len(alpha[i])-j-1)

for val in alpha_dict.values(): # dict에 저장된 수들을 모두 리스트에 추가
    numList.append(val)

numList.sort(reverse=True) # 수들을 내림차순 정렬

sum = 0
pows = 9
for i in numList: # 첫 번째 부터 가장 큰 부분을 차지하므로 9를 곱해준다
    sum += pows * i
    pows -= 1
# 내려갈수록 그 알파벳이 차지하는 비중이 적으므로 -1 
print(sum)