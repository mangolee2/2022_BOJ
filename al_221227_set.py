" 직사각형 경계선 최솟값 "
# x,y,w,h = map(int, input().split())

# a=abs(x-0)
# b=abs(w-x)
# c=abs(h-y)
# d=abs(y-0)
# li=[a,b,c,d]
# li.sort()
# print(li[0])

" 경계선 2 "
# x,y,w,h = list(map(int, input().split())) # 리스트로 받고
# print(min([x, y, w-x, h-y])) # min(괄호) 안에 반드시 [리스트] 형식 맞추기

" 네번째 점 "

# arr=[2,0,1,3,2,0,2,3,0,1,1,2,2,0,3]
# brr=[0]*4

# for item in arr:
#     brr[item] += 1
#     print(brr)
# import collections
# xli=[]
# yli=[]
# for i in range(3):
#     n,m = list(map(int, input().split()))
#     xli.append(n)
#     yli.append(m) # 리스트에 넣어주기 
# # 카운트해서 1인걸로 출력
# for i in range(3):
#     if xli.count(xli[i]) == 1:
#         x = xli[i]
#     if yli.count(yli[i]) == 1:
#         y = yli[i]
# print(x,y)

" 직각삼각형 "

# while True: # 계속 입력할거면, while True를 기억하자~
#     a = list(map(int, input().split()))
#     maxnum = max(a)
#     a.remove(maxnum)
#     if sum(a)==0:
#         break
#     elif maxnum**2 == (a[0]**2 + a[1]**2):
#         print("right")
#     else:
#         print("wrong")

" 택시 기하학 "
# import math

# r=int(input())
# print(f'{r*r*math.pi:.6f}') # 파이r제곱
# print(f'{2*r*r:.6f}')


