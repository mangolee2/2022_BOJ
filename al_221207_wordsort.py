" 단어 정렬 "

n = int(input()) # 13
word = []
for i in range(n):
    word.append(input()) # but, i, wont
word = set(word)

word = (sorted(word)) # 알파벳순 정렬
word.sort(key=lambda x:len(x))

for i in word:
    print(i)