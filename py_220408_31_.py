""" 31~ """

""" 문자열 합치기
다음 값을 예상해보시오. """

a = "3"
b = "4"
# print(a+b) # 두 문자열에 대해 덧셈 기호는 문자열의 연결을 의미한다


""" 문자열 곱하기  """
# print("Hi"*3)

# print("-"*80)

t1 = 'python'
t2 = 'java'
# print(t1+t2)
t3 = t1 + " " + t2 + " "
# print(t3*4)

""" 문자열 출력 """

name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
# print(f'이름: {name1} 나이: {age1}' )
# print(f'이름: {name2} 나이: {age2}' )

# print("이름: %s 나이: %d" % (name1, age1)) # %s : 문자열 데이터 타입의 값
# print("이름: %s 나이: %d" % (name2, age2)) # %d : 정수형 데이터 타입의 값

# print("이름: {} 나이 : {}".format(name1, age1))
# print("이름: {} 나이 : {}".format(name2, age2))

""" 컴마 제거하기 """

상장주식수 = '5,969,782,550'
nocom = 상장주식수.replace(",","")
int_ = int(nocom)
# print(int_, type(int_))

""" 문자열 슬라이싱 """

분기 = "2020/03(E) (IFRS연결)"
# print(분기.split("()"))
print(분기[:7])

""" strip 메서드 """
data = "   삼성전자   "
# strip_ = data.strip("   ") # strip() 만 사용해도 공백이 제거됨
strip_ = data.strip()
print(strip_)
