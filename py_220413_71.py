""" 71~ 튜플 """

from codecs import utf_16_be_encode


my_variable = () # 괄호 : 튜플을 정의하는 기호
# print(type(my_variable))

movie_rank = ("닥터 스트레인지", "스플릿", "'럭키")
# print(movie_rank)

tu_ = (1)
# print(type(tu_)) # int 로 인식
tu_ = (1, ) # 하나의 데이터가 저장되는 경우, 쉼표 입력!
# print(type(tu_))

# t = (1, 2, 3)
# t[0] ="a"
# print(t[0]) # 튜플은 원소의 값 변경 불가

t = 1, 2, 3, 4
# print(type(t)) # 튜플로 인식, 원칙적으로는 괄호 사용

t = ("a", "b", "c")
t = ("A", "B", "C") # 튜플 : 원소 변경 불가능 -> 새로 지정
# print(t)

interest = ("삼성전자","LG전자","SK Hynix")
data = list(interest)
# print(data)

temp = 'apple', 'banana', 'cake'
a, b, c = temp
print(a, b, c)

""" range 함수 """
data = tuple(range(2, 100, 2))
print(data)