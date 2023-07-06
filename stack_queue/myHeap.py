class MyHeap:
    def __init__(self, nums) -> None:
        self.nums = nums
        self.heapify()

    def adjustDown(self, index):
        while index * 2 + 1 < len(self.nums):
            if index * 2 + 2 < len(self.nums) and self.nums[index*2+2] > self.nums[index*2+1]:
                maxChildIndex = index * 2 + 2
            else:
                maxChildIndex = index * 2 + 1
            if self.nums[index] < self.nums[maxChildIndex]:
                self.nums[index], self.nums[maxChildIndex] = self.nums[maxChildIndex], self.nums[index]
                index = maxChildIndex
            else:
                break

    def heapify(self):
        for index in range(len(self.nums)//2-1, -1, -1):
            self.adjustDown(index)
    
    def heapInsert(self, newNum):
        self.nums.append(newNum)
        self.heapify()

    def heapPop(self):
        self.nums[0], self.nums[-1] = self.nums[-1], self.nums[0]
        self.nums.pop()
        self.heapify()

    def heapTop(self):
        return self.nums[0]

lst = [1, 4, 5, 7, 3, -3, 9, 2, 0] 
myheap = MyHeap(lst)
print('j')