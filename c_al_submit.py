""" 그리디 알고리즘 구현 문제 ( 큰 수의 법칙 ) """
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# N 개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n-1] # 가장 크 ㄴ수
second = data[n-2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K 번 더하기
        if m == 0: # m 이 0이라면 반복문 탈출
            break
        result += first
        m -=1 # m 이 0 이라면 반복물 탈출
    if m == 0: # m 이 0 이라면 반복물 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기

print(result) # 최종 답안 출력