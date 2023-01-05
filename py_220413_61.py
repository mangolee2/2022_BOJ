""" 61~ """
from sqlalchemy import intersect


price = ['20180728','100','130','140','150','160','170']
# print(price[1:])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[::2])
# for i in nums:
#     if i % 2 == 1:
#         print(i)
# print(nums[1::2])
nums = [1, 2, 3, 4, 5]
# print(nums[::-1])

interest = ['삼성전자', 'LG전자', 'Naver']
# print(interest[::2])
# print(interest[0], interest[2])
# print(interest[2])

""" join 메서드 """
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print(' '.join(interest))
# print('/'.join(interest))
# print('\n'.join(interest))

""" split 메서드 """
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
# print(interest) # list 형태가 ''붙여있으니 고려 안해도 됨

""" 리스트 정렬 """
data = [ 2, 4, 3, 1, 5, 10, 9]
data.sort()
# sort_ = data.sort() # 요건 안됨/ None 값 나옴
# print(data)

""" 또는 """
data = [ 2, 4, 3, 1, 5]
data2 = sorted(data)
print(data2)