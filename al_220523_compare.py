""" 두 수 비교하기 """
T = int(input())
# num = list(map(int, input().split()))
# # print(num)
for i in range(1, T+1):
    num = list(map(int, input().split()))
    if num[0] > num[1]:
        print(">")
    elif num[0] < num[1]:
        print("<")
    else:
        print("==")

