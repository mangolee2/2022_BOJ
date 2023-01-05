""" 수 정렬하기 2 """
import sys
n = int(input())
m = []
for i in range(n):
    m.append(int(sys.stdin.readline()))
for i in sorted(m):
    sys.stdout.write(str(i)+'\n')