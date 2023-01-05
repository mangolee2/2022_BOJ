""" 설탕 봉지 """
# li=[5,3]
# n=int(input())
# count=0
# for i in li:
#     count+=n//i
#     n=n%i
    
# print(count)

sugar=int(input())
bag=0
while sugar>=0:
    if sugar%5==0:
        bag+=(sugar//5)
        print(bag)
        break
    sugar -= 3
    bag += 1 # 5의 배수가 될 때까지 설탕 -3, 봉지+1

else:
    print(-1)