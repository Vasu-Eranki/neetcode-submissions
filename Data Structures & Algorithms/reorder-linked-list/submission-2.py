# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = head.next 
        #finding midpoint of linkedlist 
        while(fast and fast.next):
            slow = slow.next 
            fast = fast.next.next
        # slow pointer is now at midpoint 
        secondhalf = slow.next 
        slow.next = prev = None 
        while(secondhalf):
            next_head,secondhalf.next= secondhalf.next,prev
            secondhalf,prev = next_head,secondhalf
        secondhalf = prev
        while(secondhalf):
            next_of_secondhalf,next_of_head = secondhalf.next,head.next 
            head.next,secondhalf.next = secondhalf,next_of_head 
            secondhalf,head = next_of_secondhalf,next_of_head
