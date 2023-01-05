for tc in range(int(input())):
    word = list(input())
    word.sort()
    stack = []

    for i in word:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if stack:
        # print(f'#{tc + 1} {"".join(stack)}')
        print(f'#{tc + 1} {"".join(stack)}' )
    else:
        print(f'#{tc + 1} Good')



