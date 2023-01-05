" 대표값 "
data = []
for i in range(5):
    data.append(int(input()))
print(int(sum(data)//5))
data.sort() # 정렬
print(data[2])
