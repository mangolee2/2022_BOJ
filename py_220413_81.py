""" 딕셔너리 """
""" 별 표현식 
데이터 언패킹 : 변수의 개수가 달라도 언패킹 가능"""

from re import A


a, b, *c = (0, 1, 2, 3, 4, 5)
# print(a , b, c)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4 ]
# *valid_score,_ ,_ = scores
# print(valid_score)
a, *b, c = scores # 가운데 있는 8개 값
# print(a, b, c)

temp = {}

# ice = {'메로나': 1000, '플라포': 1200, '빵빠레': 1800}
# print(ice)


ice = {'메로나': 1000, '플라포': 1200, '빵빠레': 1800}

ice["죠스바"] = 1200
ice["월드콘"] = 1500
# print(ice)

ice={'메로나': 1000, 
'플라포': 1200, 
'빵빠레': 1800, 
'죠스바': 1200, 
'월드콘': 1500}

# print("메로나 가격: ", ice['메로나'])

ice['메로나'] = 1300
# print(ice)

del ice['메로나']
print(ice)