# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_pointer = None
        while(head):
            next_pointer = head.next 
            head.next = current_pointer
            current_pointer = head 
            head =next_pointer
        return current_pointer