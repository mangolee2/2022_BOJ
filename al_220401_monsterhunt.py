T = int(input())

for i in range(1 ,T+1):
    tc = list(map(int, input().split()))
    D = tc[0]
    L = tc[1]
    n = tc[2]
    res = (D*n) + (D * L * n * (n-1) * 1/200)
    print(f'#%d %d'%(i, res))