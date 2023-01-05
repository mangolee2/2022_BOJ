"""
큰값 같은깂 작은값 찾기
"""
T = int(input())

for i in range(1, T+1):
    data = list(map(int, input().split()))
    if data[0] > data[1]:
        print(f"#{i} >")
    elif data[0] == data[1]:
        print(f"#{i} =")
    else : 
        print(f"#{i} <")