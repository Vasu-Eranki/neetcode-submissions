class DoubleLinkedNode:
    def __init__(self,val:str="",prev:DoubleLinkedNode=None,next:DoubleLinkedNode=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = DoubleLinkedNode(homepage,None,None) 
        self.length = 0

    def visit(self, url: str) -> None:
        curr = self.head
        newnode = DoubleLinkedNode(url)
        curr.next = newnode
        newnode.prev = curr
        curr = curr.next 
        self.head = curr

    def back(self, steps: int) -> str:
        curr = self.head
        while(curr.prev and steps):
            curr = curr.prev
            steps-=1
        self.head = curr
        return curr.val

    def forward(self, steps: int) -> str:
        curr = self.head
        while(curr.next and steps):
            curr = curr.next
            steps-=1
        self.head = curr
        return curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)