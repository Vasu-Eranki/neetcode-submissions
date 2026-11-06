class MyHashMap:

    def __init__(self,capacity=8):
        self.bucket = [[] for _ in range(capacity)]
        self.size = 0
        self.threshold = 0.5 
        self.capacity = capacity
    def put(self, key: int, value: int) -> None:
        if (self.size/self.capacity) >=self.threshold:
            self.resize()
        # check if already present
        index = hash(key)%self.capacity
        for i,(k,v) in enumerate(self.bucket[index]):
            if k==key:
                self.bucket[index][i]=(key,value)
                return
        self.bucket[index].append((key,value))
        self.size+=1
    def get(self, key: int) -> int:
        index = hash(key)%self.capacity 
        for (k,v) in self.bucket[index]:
            if key==k:
                return v 
        return -1
    def remove(self, key: int) -> None:
        index = hash(key)%self.capacity
        for i,(k,v) in enumerate(self.bucket[index]):
            if key==k:
                self.bucket[index][i] = self.bucket[index][-1]
                self.bucket[index].pop()
                self.size-=1
    def resize(self)->None:
        self.capacity*=2
        new_bucket = [[] for i in range(self.capacity)]
        old_table = self.bucket 
        self.bucket = new_bucket 
        for bucket in old_table:
            for k,v in bucket:
                self.put(k,v)
        return



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)