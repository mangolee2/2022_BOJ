"저울"
import sys
input = sys.stdin.readline

n = int(input())
w = list(map(int, input().split()))

w.sort()
target = 1
for i in w:
    if target < i:
        break
    target += i
print(target)