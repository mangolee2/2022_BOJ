" 세탁소 사장 동혁 "

n = int(input())
unit = [25, 10, 5, 1]
count = [0]*4

for i in range(n):
    C = int(input())    
    for j in range(len(unit)):
        count[j] = C//unit[j]
        C = C%unit[j]

    print(' '.join(map(str,count)))