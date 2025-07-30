from functools import reduce

def checkMask(l):
    
    binaryStr = ''
    for _ in range(4):
        if l[_] < 0 or l[_] > 255:
            return False
        binaryStr += bin(l[_])[2:].ljust(8, '0')
    followingZero = False
    for char in binaryStr:
        if followingZero and char != '0':
            return False
        elif char == '0':
            followingZero = True
    return True


def checkIp(l):
    for _ in range(4):
        if l[_] < 0 or l[_] > 255:
            return False
    return True

def checkSubNet(ip1, ip2, mask):
    # ip1Bin, ip2Bin, maskBin = '', '', ''
    # for _ in range(4):
    #     ip1Bin += bin(ip1[_])[2:]
    # for _ in range(4):
    #     ip2Bin += bin(ip2[_])[2:]
    # for _ in range(4):
    #     maskBin += bin(mask[_])[2:]
    
    # ip1Dec = int(ip1Bin, 2)
    # ip2Dec = int(ip2Bin, 2)
    # maskDec = int(maskBin, 2)

    ip1Dec = reduce(lambda x,y: (x << 8) + y, ip1)
    ip2Dec = reduce(lambda x,y: (x << 8) + y, ip2)
    maskDec = reduce(lambda x,y: (x << 8) + y, mask)

    subnet1 = ip1Dec & maskDec
    subnet2 = ip2Dec & maskDec
    return subnet1 == subnet2

while True:
    try:
        mask = list(map(int, input().split('.')))
        ip1 = list(map(int, input().split('.')))
        ip2 = list(map(int, input().split('.')))
        if checkIp(ip1) and checkIp(ip2) and checkMask(mask):
            if checkSubNet(ip1, ip2, mask):
                print(0)
            else:
                print(2)
        else:
            print(1)
    except:
        break
