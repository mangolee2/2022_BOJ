""" 51~ """

""" 리스트 생성 """
# movie_rank = [[1, "닥터 스트레인지"], [2, "스플릿"], [3,"럭키"]]
from statistics import mean


movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
movie_rank.append("배트맨")
# mv2 = movie_rank.append("배트맨") # 이라고 변수에 저장해두면 값 안나옴 None
# print(movie_rank)

movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, '슈퍼맨')
# print(movie_rank)

# movie_rank.remove('럭키')
# del movie_rank[3]
# print(movie_rank)
# movie_rank.remove[2:4] # 안되고, 문제의도 : 이미 삭제한 인덱스 고려해서 인덱스 생각하며 삭제
del movie_rank[2]
del movie_rank[2]
# print(movie_rank)

""" langs 리스트 만들기 """
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
# print(langs) 

""" 최댓값, 최솟값 출력 """
nums = [1, 2, 3, 4, 5, 6, 7]
# print(f"max: {max(nums)} \nmin: {min(nums)}")
"""print("max: ", max(nums))
    print("min:", min(nums))"""

""" 합 출력 """
nums = [1, 2, 3, 4, 5]
# print(sum(nums))

""" 데이터의 갯수 출력 """
cook =  ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
# print(len(cook))

""" 평균 출력 """
nums = [1, 2, 3, 4, 5]
# print(mean(nums))
average = sum(nums)/len(nums) # 평균 = 합/원소 갯수
# print(average)

