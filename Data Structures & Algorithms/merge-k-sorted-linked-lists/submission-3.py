# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self,list1,list2):
        if not list1 and not list2:
            return None
        elif list1 and not list2:
            return list1
        elif not list1 and list2:
            return list2
        else:
            newnode = ListNode()
            curr = newnode
            while(list1 or list2):
                if(list1):
                    if(list2):
                        if(list1.val<=list2.val):
                            newnode.val = list1.val
                            list1 = list1.next
                        else:
                            newnode.val = list2.val 
                            list2 = list2.next
                    else:
                        newnode.val = list1.val 
                        list1 = list1.next
                else:
                    newnode.val = list2.val 
                    list2 = list2.next
                if(list1 or list2):
                    newnode.next = ListNode()
                    newnode = newnode.next
            return curr


    def mergeSort(self,lists:List[Optional[ListNode]],start:int,end:int)->Optional[ListNode]:
        if(start>end):
            return None
        if (end==start):
            return lists[start]
        mid = start + (end-start)//2
        left = self.mergeSort(lists,start,mid)
        right = self.mergeSort(lists,mid+1,end)

        return self.mergeTwoLists(left,right)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.mergeSort(lists,0,len(lists)-1)
        