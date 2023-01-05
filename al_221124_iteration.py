" 문자열 반복 "

# n=int(input())
# for i in range(n):
#     num, s = input().split() # 이게 포인트.. [0],[1] 안쓰고 첨부터 지정
#     text = '' # 문자에 담아줌 : ''
#     for i in s:
#         text += int(num)*i
#     print(text)

" 단어 공부 "

# word = input().upper()
# wordli = list(set(word))
# cnt = [] # 수 세어주고 저장 

# for i in wordli:
#     count = word.count(i)
#     cnt.append(count)
# if cnt.count(max(cnt)) >=2: # max 센 개수가 2개 이상
#     print('?')
# else:
#     print(wordli[(cnt.index(max(cnt)))])

" 단어의 갯수 "
# word = input().split()
# print(len(word)) # 스플릿으로 나누어준 단어 수 세어줌... len..

" 다이얼 "

# num = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# save = 0

# li = list(input())

# for i in li: # WA 
#     # print(i)
#     for j in num:
#         if i in j: # for 문으로 각 문자열을 돌게 해야함@! 그리고 있으면 in !!
#             save += num.index(j) + 3
# print(save)

" 크로아티아 알파벳 "
# cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# s = input()

# for i in cro:
#     s = s.replace(i, 'a')
# print(len(s))

" 그룹 단어 체커 "

# n = int(input())
# cnt = n # 3 

# for i in range(n):
#     word = input() # happy 
#     for j in range(len(word)-1): # 4 
#         if word[j] == word[j+1]: # aaa 일 경우 통과
#             pass
#         elif word[j] in word[j+1:]: # aaba 일 경우 -1 
#             cnt -= 1
#             break
# print(cnt)

" 큰 수 a+b "
# a, b = map(int, input().split())
# print(a+b)

" 부녀회장이 될테야 "
# t=int(input())

# for _ in range(t):
#     floor=int(input())
#     num=int(input())
#     f0 = [x for x in range(1, num+1)]
#     for k in range(floor):
#         for i in range(1, num):
#             f0[i] += f0[i-1]
#     print(f0[-1]) # 가장 마지막 수 출력 

" 분수찾기 "
# x=int(input())
# num_list=[]

# num=0
# num_count=0

# while num_count < x:
#     num += 1
#     num_count += num
# num_count -= num

# if num%2 == 0:
#     i = x -num_count
#     j = num-i +1 
# else:
#     i = num - (x-num_count) + 1
#     j = x - num_count

# print(f"{i}/{j}")

" 수 정렬하기 3 "

import sys
input = sys.stdin.readline

t = int(input())
numlist = [0] * 10001 # 메모리 할당해주고 

for _ in range(t):
    numlist[int(input())] += 1

for i in range(10001):
    if numlist[i] != 0:
        for j in range(numlist[i]):
            print(i)

