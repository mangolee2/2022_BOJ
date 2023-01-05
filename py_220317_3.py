""" 41 ~ upper 메서드 """

# ticker = "btc_krw"
# print(ticker.upper())
# ticker = "BTC_KRW"
# print(ticker.lower())

# s = "hello"
# print(s.capitalize())

"""  endswith 메서드 """
# file_name = "보고서.xlsxs"
# tc = file_name.endswith(("xlsx", "xls"))
# print(tc)

""" startswith 메서드 """
# file_name = "2020_보고서.xlsx"
# a =file_name.startswith("2020")
# print(a)

""" split 메서드 """
# a = "hello world"
# print(a.replace(' ', ''))

# ticker = "btc_krw"
# split_ = ticker.split('_')
# print(split_)

# date = "2020-05-01"
# split_ = date.split('-')
# print(split_)

# data = "039490     "
# empty_ = data.rstrip()
# print(empty_+'.')
# print(data.replace(' ', ''))

""" 리스트 생성 """

# movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
# # print(movie_rank)
# movie_rank.append('배트맨')
# # print(movie_rank)
# movie_rank.insert(1, '슈퍼맨')
# # print(movie_rank)
# # movie_rank.remove('스플릿')
# del movie_rank[2]
# del movie_rank[2] # 삭제된 순서 고려할 것 ~~! 
# print(movie_rank)

# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]
# langs = lang1 + lang2
# print(langs)

# nums = [1, 2, 3, 4, 5, 6, 7]
# print("max:" , max(nums))
# print("min:" , min(nums)) # + 로쓰면 더해지지 않음! not concatenate

# nums = [1, 2, 3, 4, 5]
# print(sum(nums))

# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전" ]
# print(len(cook))

# nums = [ 1, 2, 3, 4, 5]
# average_ = sum(nums)/len(nums)
# print(average_)
# print(average(nums))

""" 슬라이싱 """
# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price[1:])

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[::2])

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[1::2])  # [1:-1:2] -> [2, 4, 6, 8] 만 출력됨

# nums = [1, 2, 3, 4, 5]
# print(nums[::-1])

# interest = ['삼성전자', 'LG전자', 'Naver']
# print(interest[0], interest[2])
# odd = interest[::2]
# print(odd)

""" join 메서드 """
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# # print(interest[0], interest[1], interest[2], interest[3], interest[4])
# print(" ".join(interest))
# print("/".join(interest))
# print("\n".join(interest))

""" 문자열 split 메서드 """
string = "삼성전자/LG전자/Naver"