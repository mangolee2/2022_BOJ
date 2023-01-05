""" 행렬 """

n, m = map(int, input().split())
a_matrix = []
b_matrix = []
for i in range(n):
    for j in range(m):
        a_matrix.append(int(input()))
        b_matrix.append(int(input()))

cnt = 0
 # 3x3 행렬 변환함수 생성
def convert_matrix(i, j, arr):
   for x in range(i, i+3):
       for j in range(j, j+3):
           arr[x][y] == 1 - arr[x][y]

for i in range(n-2):
    for j in range(m-2):
        if change_matrix[i][j] 

for i in range(n):
    for j in range(m):
        if change_matrix[i][j] != answer_matrix[i][j]:
            non_answer = -1

if non_answer == -1:
    print(non_answer)
else:
    print(cnt)