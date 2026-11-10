class DoubleLinkedListNode:
    def __init__(self,val=0):
        self.val = val 
        self.prev = None 
        self.next = None 



class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.capacity = capacity 
        self.size = 0
        self.head = DoubleLinkedListNode(0)
        self.tail = DoubleLinkedListNode(0)
        self.head.next = self.tail 
        self.tail.prev = self.head 
    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1    
        node = self.hashmap[key]
        _,value = node.val 
        new_node = DoubleLinkedListNode((key,value))
        self.insert(new_node) # move it to the front 
        self.delete(node) # remove a copy from the back
        self.hashmap[key]=new_node # update reference in hashmap
        return value
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.delete(node)
            new_node = DoubleLinkedListNode((key,value))
            self.insert(new_node)
            self.hashmap[key] = new_node
        else:
            node = DoubleLinkedListNode((key,value))
            self.hashmap[key]=node
            self.insert(node)
            if self.size>self.capacity:
                key = self.remove_least_used_element()
                del self.hashmap[key]
        return   

    def remove_least_used_element(self):
        node_we_want_delete = self.tail.prev
        key,value = node_we_want_delete.val 
        self.delete(node_we_want_delete)
        return key

    def delete(self,node):
        node_prev= node.prev 
        node_next = node.next 
        node_prev.next = node_next 
        node_next.prev = node_prev 
        self.size-=1
        return
    def insert(self,node):
        next_head = self.head.next 
        self.head.next = node 
        node.prev = self.head
        node.next = next_head
        next_head.prev = node
        self.size+=1
        return 



        
