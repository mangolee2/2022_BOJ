""" 한수 (각 자리의 차이가 일정할 때, 등차수열이라..?) """

def getHansu(N):
    if N < 100:
        hansu = N
    else:
        hansu = 99
        for i in range(100, N+1):
            numList = list(map(int, str(i)))
            if numList[0] - numList[1] == numList[1] - numList[2]:
                hansu += 1
    return hansu

if __name__ == "__main__":
    num = int(input())
    print(getHansu(num))