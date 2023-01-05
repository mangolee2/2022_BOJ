""" dynamic algorithm """

""" 
# 입력 조건
1. 첫째 줄에 N, M 이 주어진다.
2. 이후의 N 개의 줄에는 각 화폐의 가치가 주어진다. 화폐의 가치는 10,000보다 작거나 같은 자연수이다.

# 출력 조건
1. 첫째 줄에 경우의 수 X를 출력한다.
2. 불가능할 때는 -1을 출력한다.
"""

n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(array
     -
     [i],m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])