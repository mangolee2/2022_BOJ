import base64

# sitename = 'webisfree'
# sitename_bytes = sitename.encode('ascii')
# sitename_base64 = base64.b64encode(sitename_bytes)
# sitename_base64_str = sitename_base64.decode('ascii')

# print(sitename_base64_str)

# sitename_base64_str = 'U3VzcGljaW9uIGZvbGxvd3MgY2xvc2Ugb24gbWlzdHJ1c3Qu'
# sitename_bytes = base64.b64decode(sitename_base64_str)
# sitename = sitename_bytes.decode('ascii')
# print(sitename)

T = int(input())

for test_case in range(1, T+1):
    s = input() 
    s_bytes = base64.b64decode(s)
    ss = s_bytes.decode('ascii')    
    print(f'#{test_case} {ss}')
