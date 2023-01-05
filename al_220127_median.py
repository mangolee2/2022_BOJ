""" 중앙값(median) 찾기 : 정렬하여 중간에 위치한 값 찾기 """
T = int(input())
nums = list(map(int, input().split()))
# 9 <= nums <= 199
# nums % 2 != 0 
nums.sort() # sort 함수를 써서 정렬
index_num = (T-1)//2
print("{}".format(nums[index_num]))