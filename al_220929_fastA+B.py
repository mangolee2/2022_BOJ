""" 빠른 A+B """
import sys

input = sys.stdin.readline
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    sum=a+b
print(sum)