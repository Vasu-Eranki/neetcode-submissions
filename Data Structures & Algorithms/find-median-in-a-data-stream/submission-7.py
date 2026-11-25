class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []  
        self.totalelements = 0      
        return
    def reBalance(self)->None:
        if len(self.maxheap)>len(self.minheap):
            while(len(self.maxheap)>len(self.minheap)):
                value = heapq.heappop_max(self.maxheap)
                heapq.heappush(self.minheap,value)
                return
        while(len(self.minheap)>len(self.maxheap)):
            value = heapq.heappop(self.minheap)
            heapq.heappush_max(self.maxheap,value)
        return
    def addNum(self, num: int) -> None:
        if self.minheap and num>self.minheap[0]:
            heapq.heappush(self.minheap,num)
        else:
            heapq.heappush_max(self.maxheap,num)
        len_minheap = len(self.minheap)
        len_maxheap = len(self.maxheap)
        self.totalelements+=1
        if abs(len_minheap-len_maxheap)>1:
            self.reBalance()
        return
    def findMedian(self) -> float:
        if self.totalelements%2: # odd number of entries
            if len(self.minheap)>len(self.maxheap):
                return self.minheap[0]
            return self.maxheap[0]
        minvalue = self.minheap[0]
        maxvalue = self.maxheap[0]
        return (minvalue+maxvalue)/2

        
        