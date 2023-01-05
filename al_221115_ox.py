" OX 퀴이즈 "

n = int(input())

for i in range(n):
    data = input()
    sum = 0 # 수를 어케 세지? sum = 0 변수를 만들어둠
    cnt = 1 
    for i in data:
        if i == 'O':
            sum += cnt
            cnt += 1
            # print(sum, cnt)
        else:
            cnt = 1
    print(sum)