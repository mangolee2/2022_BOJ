T = int(input())
for i in range(T):
    k = int(input())
    s = list(map(int, input().split(" ")))
    ans = 0
    for j in range(1, len(s)-1):
        if s[j] != min(s[j], s[j-1], s[j+1]) and s[j] != max(s[j], s[j-1], s[j+1] ):
           ans += 1
    print("#%d %d" %((i+1), ans))