List = []

for i in range(1, 10):
    for j in range(1, 10):
        List.append(i*j)

myList = list(set(List))

T = int(input())
for i in range(1, T+1):
    num = int(input())
    if num in myList:
        print(f"#{i} Yes")
    else:
        print(f"#{i} No ")
