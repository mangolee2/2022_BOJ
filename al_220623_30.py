""" 미르코가 좋아하는 30 """

n = list(input())
n.sort(reverse=True) # 무조건 큰 수를 해주면 됨? ㅇㅇ, 
# 어차피 다 더해서 3이 아니면 땡 탈락이고 하니 reverse = True 로 해준다
sum = 0
for i in n: # 리스트로 해줘서 in n 가능
    sum += int(i)
    # print(sum)
if (sum%3) != 0 or "0" not in n:
    print("-1")
else:
    # print(n) #['2', '1', '0']
    print(''.join(n))