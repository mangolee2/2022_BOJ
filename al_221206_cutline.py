" 커트라인 "

n, k = map(int, input().split()) # 5 2
data = list((map(int, input().split()))) # 100 76 85 93 98 
data.sort(reverse=True) # 오름차순 정렬
print(data[k-1])