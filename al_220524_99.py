""" 구구단 출력 """
N = int(input())
for i in range(1, 10):   
    print(f'{N} * {i} = {N*i}')

""" another one """
for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i} * {j} = {i*j}')