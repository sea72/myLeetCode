def check(pw):
    if len(pw) < 8:
        return False
    
    upperCase, lowerCase, num, weird = 0, 0, 0, 0
    for char in pw:
        ascii = ord(char)
        if 48 <= ascii <= 57:
            num = 1
        elif 65 <= ascii <= 90:
            upperCase = 1
        elif 97 <= ascii <= 122:
            lowerCase = 1
        elif 33 <= ascii <= 126:
            weird = 1
    if upperCase + lowerCase + num + weird <=2:
        return False
    
    show = {}
    for i in range(0, len(pw)-2):
        if pw[i:i+3] not in show:
            show[pw[i:i+3]] = i
        elif i - show[pw[i:i+3]] >= 3:
            return False
    return True



while True:
    try:
        pw = input()
        if pw:
            if check(pw):
                print('OK')
            else:
                print('NG')
    except:
        break
