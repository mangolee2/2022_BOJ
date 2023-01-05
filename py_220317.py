""" 21~ 문자열 인덱싱 """

# letters = 'python'
# print(letters[0])
# print(letters[2])
# print(letters[0], letters[2])

""" 문자열 슬라이싱 """
# license_plate = "24가 2210"
# print(license_plate[-4:])


""" 문자열 인덱싱 """
# string = "홀짝홀짝홀짝"
# print(string[::2]) # 시작인덱스:끝인덱스:오프셋!!!
# for i in string:
#     if i == "홀":
#         print(i)


""" 문자열 슬라이싱 """
# string = "PYTHON"
# print(string[::-1])

""" 문자열 치환 """
# phone_number = "010-1111-2222"
# phone_number1 = phone_number.replace('-',' ')
# print(phone_number1)
# print(phone_number.replace('-', ' '))

# phone_number2 = phone_number1.replace(' ','')
# print(phone_number2)

# url = "http://sharenook.kr"
# url_split = url.split('.')
# print(url_split[-1])

""" 문자열은 immutable """
# lang = 'python'
# lang[0] = 'P'  # 문자열은 수정이 불가하시다!!
# print(lang)

# string = 'abcdfe2a354a32a'
# string1 = string.replace('a','A')
# print(string1)


string = 'abcd'
# string1 = string.replace('b', 'B') # 변수로 지정하면, aBcd 가 나오지만.
string.replace('b', 'B')  # 변수 지정 안 할 경우, abcd 가 나온다~!
print(string) 