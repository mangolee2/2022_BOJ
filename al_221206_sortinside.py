" 소트인사이드 "

n=int(input())
data = []
for i in str(n): # 하나하나 str 돌면서 
    data.append(i)
    data.sort(reverse=True) 
print(''.join(data))