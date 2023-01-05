""" 5와 6의 차이 """
import sys

input=sys.stdin.readline

a,b = input().split()
min = int(a.replace('6','5')) + int(b.replace('6','5')) # 문자열 사용하는 replace
max = int(a.replace('5','6')) + int(b.replace('5','6'))

print(min, max)