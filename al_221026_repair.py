""" 수리공 항승 """

n, l = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

start=data[0]
cnt = 1

for location in data[0:]:
    if location in range(start, start+l):
        continue
    else:
        start = location
        cnt += 1

print(cnt)