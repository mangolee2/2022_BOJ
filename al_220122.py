""" 배열에서 특정 요소 찾기 """
# 다음과 같은 숫자로 이루어진 배열이 있을 때, 이 배열 내에 특정 숫자가 존재한다면 True, 존재하지 않다면 False를 반환하시오.
# def is_number_exist(number, array):
#     number = 3
#     array = [ 3, 5, 6, 1, 2, 4]
#     for number in array:    
#         if number in array:
#             return True

from sympy import multiplicity


def is_number_exist(number, array):
    for element in array:
        if number == element:
            return True
    return False


# 컴파일 후 변수에 담아두기
result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3,[3,5,6,1,2,4]))
print("정답 = Flase 현재 풀이 값 =", result(7,[6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2,[6,9,2,7,1888]))

""" 곱하기 or 더하기 """
# def find_max_plus_or_multiply(array):
#     for i in array:
#         for j in array:
#             if i >= j:
#                 return i * j
#             else:
#                 return i+j

def find_max_plus_or_multiply(array):
    multiply_sum = 0
    for number in array:
        if number <= 1 or multiply_sum <= 1:
            multiply_sum += number
        else:
            multiply_sum *= number
    return multiply_sum

result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))