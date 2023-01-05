" 소수 최소값과 합 "

m = int(input())
n = int(input())
prime = []
for i in range(m , n+1):
    if i != 1:
        check = True
        for j in range(2, i):
            if i % j == 0:
                check = False
                break # 잠깐 스탑! 
        if check:
            prime.append(i) # prime 리스트에 append 시켜주므!

if len(prime) == 0: # 길이가 0 일경우, 소수가 하나도 없단.. 의미
    print(-1)
else:
    print(sum(prime)) # 정답 출력시에도 m,n 과 마찬가지로 따로따로 지정 
    print(min(prime))
