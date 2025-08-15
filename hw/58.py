class myHeap:
    def __init__(self, list):
        self.list = list
        self.heapify()

    def heapify(self):
        for i in range(len(self.list)//2-1, -1, -1):
            self.heapAdjustDown(i)


    def heapAdjustDown(self, i):
        while i*2+1 < len(self.list):
            if i*2+2 < len(self.list) and self.list[i*2+2] < self.list[i*2+1]:
                aim = i*2+2
            else:
                aim = i*2+1
            if self.list[i] > self.list[aim]:
                self.list[i], self.list[aim] = self.list[aim], self.list[i]
            else:
                break
    
    def heappush(self, j):
        self.list.append(j)
        self.heapify()
    
    def heappop(self):
        self.list[0], self.list[-1] = self.list[-1], self.list[0]
        temp = self.list.pop()
        self.heapify()
        return temp
    
    def nsmallest(self, n):
        tmp = []
        while n > 0:
            tmp.append(self.heappop())
            n -= 1
        return tmp

lst = [98, 243, 44, 65, 34, 5, 2, 78, 92, 233]
heap = myHeap(lst)
print(heap.nsmallest(5))