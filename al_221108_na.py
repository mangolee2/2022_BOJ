' 성적이 낮은 순으로 학생 출력하기 '
# n = int(input())
# array = []

# for i in range(n):
#     data = input().split() # 문자열이 포함되어 있으면 input값으로 받고, 띄어쓰기로 구분해줌
#     array.append((data[0], int(data[1])))  # 문자열과 숫자로 각각 저장

# array = sorted(array, key = lambda x:x[1])

# for j in array:
#     print(j[0], end=' ')

'두 배열의 원소 교체'

n, k = map(int, input().split())
a=list((map(int, input().split())))
b=list((map(int, input().split())))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break      
print(sum(a))  