class Node():
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

inStr = list(map(int, input().split()))

n = inStr[0]
head = Node(inStr[1])

for no in range(2, n*2, 2):
    a, b = inStr[no], inStr[no+1]
    after = Node(a)
    cur = head
    while cur.value != b:
        cur = cur.next
    after.next = cur.next
    cur.next = after

if head.value == inStr[-1]:
    head = head.next
else:
    cur = head
    while cur.next.value != inStr[-1]:
        cur = cur.next
    cur.next = cur.next.next

cur = head
while cur:
    print(cur.value, end=" ")
    cur = cur.next