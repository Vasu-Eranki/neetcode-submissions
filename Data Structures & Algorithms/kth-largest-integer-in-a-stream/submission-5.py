class MinHeap:
    def __init__(self,k):
        self.heap = [0]
        self.heapsize = k
    def top(self):
        if len(self.heap)>1:
            return self.heap[1]
        return None
    def push(self,x:int):
        self.heap.append(x)
        i = len(self.heap)-1
        while(i>1 and self.heap[i]<self.heap[i//2]):
            self.heap[i//2],self.heap[i] = self.heap[i],self.heap[i//2]
            i=i//2
        diff = len(self.heap)-self.heapsize-1
        for _ in range(diff):
            self.pop()
        return
    def heapify(self,arr:List[int]):
        if not arr:
            return
        arr.append(arr[0])
        length_of_tree = (len(arr)-1)//2
        self.heap = arr
        for curr in range(length_of_tree,0,-1):
            i = curr
            while(2*i<len(self.heap)):
                if(2*i+1<len(self.heap) and 
                self.heap[2*i+1]<self.heap[2*i] and 
                self.heap[i]>self.heap[2*i+1]):
                    self.heap[2*i+1],self.heap[i] = self.heap[i],self.heap[2*i+1]
                    i = 2*i+1
                elif self.heap[i]>self.heap[2*i]:
                    self.heap[2*i],self.heap[i] = self.heap[i],self.heap[2*i]
                    i = 2*i
                else:
                    break
        diff = len(self.heap)-self.heapsize-1
        for _ in range(diff):
            self.pop()
        return
    def pop(self):
        if len(self.heap)==1:
            return None
        elif len(self.heap)==2:
            return self.heap[1]
        else:
            result = self.heap[1]
            self.heap[1] = self.heap.pop()
            index = 1
            while(2*index<len(self.heap)):
                if 2*index+1<len(self.heap) and self.heap[2*index+1]<self.heap[2*index] and self.heap[index]>self.heap[2*index+1]:
                    self.heap[2*index+1],self.heap[index] = self.heap[index],self.heap[2*index+1]
                    index = 2*index+1
                elif self.heap[index]>self.heap[2*index]:
                    self.heap[2*index],self.heap[index] = self.heap[index],self.heap[2*index]
                    index = 2*index
                else:
                    break
            return result
    def __len__(self):
        return len(self.heap) 


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.minheap = MinHeap(k)
        self.minheap.heapify(nums)
    def add(self, val: int) -> int:
        self.minheap.push(val)
        return self.minheap.top()
        
