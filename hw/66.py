comDict = {
    "reset":"reset what",
    "reset board":"board fault",
    "board add":"where to add",
    "board delete":"no board at all",
    "reboot backplane":"impossible",
    "backplane abort":"install first"
}

while True:
    try:
        cmd = input()
        hasMatched = []
        for i, j in comDict.items():
            partCmd = cmd.split()
            partIns = i.split()
            if len(partCmd) != len(partIns):
                continue
            else:
                for partNo in range(len(partCmd)):
                    if partIns[partNo].find(partCmd[partNo]) != 0:
                        break
                else:
                    hasMatched.append(j)
        if len(hasMatched) == 1:
            print(hasMatched[0])
        else:
            print('unknown command')
    except IOError:
        break