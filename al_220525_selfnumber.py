""" 셀프 넘버 """

oriNum = set(range(1, 100001))
genNum = set()

for i in range(1, 100001):
    for j in str(i): # 85 입력시,         i 를 str 으로 바꿔줌 
        i += int(j)  # 85 에 + 8 + 5 되도록 
    genNum.add(i)

selfNum = sorted(oriNum - genNum)
# selfNum.sort()
for i in selfNum:
    print(i)