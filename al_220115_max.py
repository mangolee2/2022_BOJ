""" 최댓값 찾기 """

# array = [3, 5, 6, 1, 2, 4]
# def find_max_num(arrray):
#     max_num = array[0]
#     for num in array:
#         if num > max_num:
#             max_num = num
#     return max_num

# print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]) )
# print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]) )

array = [6, 9, 2, 7, 1888]
def find_max_num(arrray):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    return max_num

# print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]) )



""" 알파벳 빈도수 찾기 """
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0]*26 # 길이가 26인 0으로 초기화된 배열을 만듦

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a') # 문자를 숫자로 바꿀 때 : "python char to ascii code" : ord 써라 나옴 -> ord() 이용
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array
print(find_alphabet_occurrence_array("apple is delicious"))

        # 정답 = find_alphabet_occurrence_array("Hello my name is sparta")) 에는 이 문자열이, 현재풀이 값에는 요 문자열이 들어가서 답이 다름
# print("정답 = [3, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 2, 2, 1, 1, 1, 0, 1, 2, 1, 0, 0, 0, 0, 1, 0] \n현재 풀이 값 =", find_alphabet_occurrence_array("Sparta coding club") )



""" 최빈값 찾기 """
def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
    max_occurrence = 0  # 0으로 초기화
    max_alphabet = alphabet_array[0] # array[0] 을 최빈값 변수에 넣어놓음

    for alphabet in alphabet_array:
        occurrence = 0
        for char in string:
            if char == alphabet:
                occurrence += 1
        if occurrence > max_occurrence:
            max_alphabet = alphabet
            max_occurrence = occurrence
    return max_alphabet

result = find_max_occurred_alphabet 
# print("정답 = a \n현재 풀이 값 =", result("Hello my name is sparta"))
# print("정답 = a \n현재 풀이 값 =", result("Sparta coding club"))
# print("정답 = s \n현재 풀이 값 =", result("best of best sparta"))

def find_max_occured_alphabet(string): 
    alphabet_occurrence_array = []

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    max_occurance = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[arr_index]
        if alphabet_occurrence > max_occurance:
            max_occurance > max_occurance
            max_alphabet_index > index

    return chr(max_alphabet_index + ord('a'))

result = find_max_occurred_alphabet
# print("정답 = a 현재 풀이 값 =", result("Hello my name is sparta"))
# print("정답 = a 현재 풀이 값 =", result("Sparta coding club"))
# print("정답 = s 현재 풀이 값 =", result("best of best sparta"))