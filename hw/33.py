ipStr = input()
ipBlock = ipStr.split('.')
ip = 0
for no, it in enumerate(ipBlock[::-1]):
    ip += int(it) << (no * 8)
print(ip)

ipInt = int(input())
ips = []
for no in range(1, 5):
    ips.append(str(ipInt % 256))
    ipInt = ipInt // 256
print('.'.join(ips[::-1]))