cmds = input().split(";")
startX, startY = 0, 0

moves = {'W':(0, 1),
         'S':(0,-1),
         'A':(-1,0),
         'D':(1,0)
         }

for cmd in cmds:
    if len(cmd) > 1 and cmd[0] in "WSAD":
        try:
            directions = cmd[0]
            d = int(cmd[1:])
            if 0 < d < 100:
                startX, startY = startX + d * moves[directions][0], startY + d * moves[directions][1]
        except:
            pass

print(f'{startX},{startY}')
