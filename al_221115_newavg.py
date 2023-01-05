" 평균 "

n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True) # 80 60 40 
m = data[0]
new = []
for i in data:
    i = i/m*100
    new.append(i)
print(sum(new)/len(new))
