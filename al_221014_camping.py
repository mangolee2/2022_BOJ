""" 캠핑 """

i = 1

while True:
    l, p, v = map(int, input().split())
    
    if l+p+v == 0: # l,p,v가 0일 때 종료되도록 하고 
        break

    tmp = v//p
    ans1 = tmp * l
    ans2 = v%p
    sum = ans1 + ans2
   
    print('Case {}: {}'.format(i, sum))
    i += 1