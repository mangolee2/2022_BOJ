" 알파벳 찾기 "
from string import ascii_lowercase

al = list(input()) # baekjoon
alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in alpha:
    if i in str(al):
        print(al.index(i), end=' ')
    else:
        print(-1, end=' ')