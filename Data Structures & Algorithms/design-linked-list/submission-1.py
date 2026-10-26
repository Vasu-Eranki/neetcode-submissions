class LinkedNode:
    def __init__(self,val:int=0,next:"LinkedNode"=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None 
        self.length = 0

    def get(self, index: int) -> int:
        if(index>=self.length):
            return -1
        curr = self.head 
        for i in range(index):
            curr = curr.next 
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        newnode = LinkedNode(val)
        curr = self.head
        newnode.next = curr
        self.head = newnode
        self.length+=1
        return  
        

    def addAtTail(self, val: int) -> None:
        newnode = LinkedNode(val)
        curr = self.head
        while(curr.next):
            curr = curr.next
        curr.next = newnode
        self.length+=1
        return 
        

    def addAtIndex(self, index: int, val: int) -> None:
        if(index>self.length):
            return 
        elif(index==self.length):
            self.addAtTail(val)
        else:
            curr = self.head
            newnode = LinkedNode(val)
            for i in range(index-1):
                curr = curr.next
            newnode.next = curr.next
            curr.next = newnode
            self.length+=1
        return

    def deleteAtIndex(self, index: int) -> None:
        print(index,self.length)
        if(index>=self.length):
            return
        elif(index<0):
            return
        else:            
            curr = self.head
            for i in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
        self.length-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)