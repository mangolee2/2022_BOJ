""" N 과 M
백트래킹 문제 """
N, M = map(int, input().split())
for i in range(N):
    for j in range(M):



n, m = int(input())
s =  []

for i in range(1, n+1):
    s.append(i)
    f()
    s.pop()

if len(s) == m:
    print(' '.join(map(str, s)))
if i in s:
    continue
