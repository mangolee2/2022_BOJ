"""
중앙값 찾기
"""
T = int(input())
nums = list(map(int, input().split()))
nums.sort()
index_num = (T-1)//2
print("{}".format(nums[index_num]))