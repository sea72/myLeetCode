import sys

def isLegalIP(blocks):
    for block in blocks:
        if not block:
            return False
        block = int(block)
        if block < 0 or block > 255:
            return False
    return True

def isLegalMask(blocks):
    followZero = False
    for no, block in enumerate(blocks, start=0):
        if not block:
            return False
        block = int(block)
        if block < 0 or block > 255:
            return False
        if no == 0:
            if block not in (255, 254, 252, 248, 240, 224, 192, 128):
                return False
            if block == 0:
                followZero = True
        if no > 0:
            if followZero and block != 0:
                return False
            if block == 0 or block in (254, 252, 248, 240, 224, 192, 128):
                followZero = True
                continue
            if block not in (255, 254, 252, 248, 240, 224, 192, 128):
                return False

    return True if blocks[-1] != '255' else False

aNum, bNum, cNum, dNum, eNum, err, private = 0, 0, 0, 0, 0, 0, 0

while True:
    try:
        str = input()
        if not str:
            break
        mid = str.index('~')
        ipStr, maskStr = str[:mid], str[mid+1:]
        ipBlocks = ipStr.split('.')
        maskBlocks = maskStr.split('.')
        if isLegalIP(ipBlocks):
            ip = [ int(block) for block in ipBlocks]
            if ip[0] in (127, 0):
                continue
            if isLegalMask(maskBlocks):
                mask = [ int(block) for block in maskBlocks]
                a,b,c,d = ip
                if 1 <= a <= 127:
                    if a == 10:
                        private += 1
                    aNum += 1
                if 128 <= a <= 191:
                    if a == 172 and 16 <= b <= 31:
                        private += 1
                    bNum += 1
                if 192 <= a <= 223:
                    if a == 192 and b == 168:
                        private += 1
                    cNum += 1
                if 224 <= a <= 239:
                    dNum += 1
                if a >= 240:
                    eNum += 1
            else:
                err += 1

        else:
            err += 1        

    except:
        break

print(aNum, bNum, cNum, dNum, eNum, err, private)
