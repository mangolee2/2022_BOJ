""" 주유소 """

# import sys
# input = sys.stdin.readline

# n=int(input())
# roads=list(map(int,input().split()))
# costs=list(map(int,input().split()))

# min_price = roads[0] * costs[0] # 우선 첫번째 값은 무조건 더해주니, 설정해주고
# min_cost = costs[0] # 첫번째 주유소 이후에 값싼 주유소 저장 

# for i in range(n-1):
#     if min_cost > costs[i]:
#         min_cost = costs[i]
    
#     min_price += min_cost * roads[i]

# print(min_price)



# ans = 0
# m = costs[0]
# for i in range(n-1):
#     if costs[i] < m:
#         m = costs[i]
#     ans += m*costs[i]
# print(ans)
N = int(input())

roads = list(map(int,input().split()))
costs = list(map(int,input().split()))

min_price = roads[0] * costs[0] # 첫번째 주유소는 무조건 +
min_cost = costs[0] # 그 다음부터 값이 싼 주유소

for i in range(1, N-1):# 0 이후부터 시작해서 그 전까지! (마지막 주유소는 안 들름)
  if min_cost > costs[i]: # 가장 값이 싼 주유소가 현재 주유소 보다 비싸면 바꿔준다.
    min_cost = costs[i] # 값 싼 주유소로 바꿔주기
  
  min_price += min_cost * roads[i]

print(min_price)