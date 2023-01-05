# array = [3, 5, 6, 1, 2, 4]
# def find_max_num(array):
#     max_num = 0
#     num = 0
#     for num in array:
#         if num > max_num:
#             max_num = num
#     return max_num
# print(max_num)

"""최댓값 찾기"""
array = [3, 5, 6, 1, 2, 4]
# def find_max_num(array):
#     for num in array:
#         for compare_num in array:
#             if compare_num > num:
#                 break
#         else: # 보면 for 에 맞춤, for~else 구문은 for문에서 break가 발생하지 않았을 경우의 동작을 else문에 적어주는 것
#             return num
# print(find_max_num([3, 5, 1, 6, 2])) # print 할 때에도 함수를 호출하고서 값을 넣어줘야 값이 나옴, 그냥 print(값)은 안됨.

def find_max_num(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
            # return max_num : 5가 출력
    return max_num # for~return 다 돌고나서 값 반환 
# print(find_max_num(array))

"""알파벳 빈도수 찾기"""
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26 # 알파벳 갯수만큼 

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char)-ord('a')
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array
# print(find_alphabet_occurrence_array('apple'))

"""최빈값 찾기"""
def find_alphabet_occurrence_array(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
    max_occurrence = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurrence = 0
        for char in string:
            if char == string:
                occurrence += 1
            
        if occurrence > max_occurrence:
            max_alphabet = alphabet
            max_occurrence = occurrence

