class DoubleLinkedListNode:
    def __init__(self,key=0,val=0):
        self.key = key 
        self.val = val 
        self.prev = None 
        self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.capacity = capacity 
        self.head = DoubleLinkedListNode(0,0)
        self.tail = DoubleLinkedListNode(0,0)
        self.head.next = self.tail 
        self.tail.prev = self.head
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            value = node.val
            self.remove(node)
            new_node = DoubleLinkedListNode(key,value)
            self.hashmap[key] = new_node
            self.insert(new_node)
            return value
        return -1    

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
        new_node = DoubleLinkedListNode(key,value)
        self.hashmap[key]=new_node
        self.insert(new_node)
        if self.size>self.capacity:
            node_to_remove = self.tail.prev
            key = node_to_remove.key 
            del self.hashmap[key]
            self.remove(node_to_remove)
        return
    def insert(self,node):
        next_node = self.head.next 
        node.prev = self.head 
        self.head.next = node
        node.next = next_node
        next_node.prev = node
        self.size+=1
        return
    def remove(self,node):
        prev_node = node.prev 
        next_node = node.next 
        prev_node.next = next_node
        next_node.prev = prev_node 
        self.size-=1
        return 
