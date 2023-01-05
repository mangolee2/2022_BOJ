n, m = map(int, input().split())
d = min(n, m)
a = []

for i in range(n):
    for j in range(m):
        for k in range(a):
            if [i,j]==[i,j+k]==[j+k, j]==[i+k, j+k]:
                print(d**2)