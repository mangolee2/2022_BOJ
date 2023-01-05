""" 캥거루 세마리2 """

# t=int(input())

# for i in range(1, t+1):
#     a, b, c = list(map(int,input().split()))
    
#     if b-a > c-b:
#         print(b-a-1)
#     else:
#         print(c-b-1)

""" 캥거루 세마리2 """
while True:
    try:
        a,b,c=list(map(int,input().split()))
        print(max(b-a, c-b)-1)
    except:
        break