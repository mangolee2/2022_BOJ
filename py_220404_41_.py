""" upper 메서드 """

ticker = "btc_krw"
# print(ticker.upper()) 
ticker1 = ticker.upper()
# print(ticker1)

""" lower 메서드 """
ticker = "BTC_KRW"
ticker2 = ticker.lower()
# print(ticker2)

""" capitalize 메서드 """
# cha_ = "hello"
# print(cha_.capitalize())
a = "hello"
a = a.capitalize()
# print(a)

""" endwith 메서드 """
file_name = "보고서.xlsx"
# print(file_name.endswith("xlsx"))

# end_ = file_name.endswith(("xlsx", "xls")) # 괄호 차이가 뭐지? 하나만 하면 에러
# 괄호 2개 써야 
# print(end_)

end3 = file_name.endswith((("xlsx", "xls", "hwp")))
# print(end3)
# 요 메서드는 문자열 갯수에 따라 괄호 수 맞춰줌니다

""" startswith 메서드 """
file_name ="2020_보고서.xlsx"
# print(file_name.startswith("2020"))

""" split 메서드 """
a = "hello world"
# print(a.split(" "))

ticker = "btc_krw"
# print(ticker.split("_"))

date = "2020-05-01"
# print(date.split("-"))

data = "039490     "
print(data.rstrip())