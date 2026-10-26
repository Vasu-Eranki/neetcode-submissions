class Solution:
    def mergeSort(self,array:List[int],start:int,end:int)->None:
        if(end-start)<=1:
            return 
        mid = start + (end-start)//2
        self.mergeSort(array,start,mid)
        self.mergeSort(array,mid,end)
        left_array = array[start:mid]
        right_array = array[mid:end]
        left_counter = 0 
        right_counter = 0
        counter = 0 
        while(left_counter<len(left_array)) and (right_counter<len(right_array)):
            if(left_array[left_counter]<=right_array[right_counter]):
                array[counter+start] = left_array[left_counter]
                left_counter+=1
            else:
                array[counter+start] = right_array[right_counter]
                right_counter+=1
            counter+=1
        while(left_counter<len(left_array)):
            array[counter+start] = left_array[left_counter]
            left_counter+=1
            counter+=1
        while(right_counter<len(right_array)):
            array[counter+start] = right_array[right_counter]
            right_counter+=1
            counter+=1
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        self.mergeSort(nums1,0,m+n)
        return
        