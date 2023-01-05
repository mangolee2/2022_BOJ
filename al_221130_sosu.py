" 소수 "

n = int(input()) # 4
sosu = list(map(int, input().split())) # 13 5 7

def prime(num): # 소수 판별 함수 만듦 
    if num ==1 :
        return False
    elif num ==2: # 유일한 짝수
        return True
    for i in range(2, num): # 소수는 홀수 3 5 7 9 11 13 ..
        if num%i == 0: # 짝수인 경우 false 
            return False
    return True # true 만 세어줌
cnt = 0
for i in sosu:
    if prime(i): # prime i가 true 이면, 
        cnt += 1
print(cnt)