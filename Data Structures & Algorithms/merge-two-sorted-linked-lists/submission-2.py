# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(not list1 and not list2):
            return list1
        result = ListNode()
        copy_of_result = result
        while(list1 or list2):
            if(list1 and list2):
                if(list1.val<=list2.val):
                    value= list1.val
                    list1 = list1.next
                else:
                    value = list2.val
                    list2 = list2.next
            elif list1:
                value = list1.val
                list1 = list1.next
            else:
                value = list2.val
                list2 = list2.next
            result.val = value


            if (list1 or list2):
                result.next = ListNode()
                result = result.next
        return copy_of_result