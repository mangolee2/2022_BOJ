" 통계학 "
from collections import Counter
import sys
input = sys.stdin.readline

n=int(input())
data=[]
for i in range(n): # 5
    data.append(int(input()))
data.sort() # 정렬

print(round(sum(data)/n)) # int 를 빼주니 잘 출력됨...
print(data[n//2])

cnt = Counter(data).most_common(2) # 카운터 이용해서, 빈도수 높은 수 2개 겟함
# 최빈값을 구합시다
if len(data) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])


print(data[-1]-data[0]) 
