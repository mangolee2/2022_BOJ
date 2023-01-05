alphabets = input()
converted_numbers = []

for alphabet in alphabets:
    converted_numbers.append(str(ord(alphabet) - ord('A')+1)) # list에만 .append 가능
print(" ".join(converted_numbers)) # .join 쓰려면 str 으로 해야됨
# print(converted_numbers.split(" "))