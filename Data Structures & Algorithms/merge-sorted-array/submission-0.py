class Solution:
    def mergeSort(self,array:List[int],start:int,end:int)->None:
        '''
        Implementation of MergeSort
        '''
        if abs(start-end)<=1:
            return 
        mid = (start+end)//2
        self.mergeSort(array,start,mid)
        self.mergeSort(array,mid,end)
        left_array = array[start:mid]
        right_array = array[mid:end]
        left_pointer = 0
        right_pointer = 0
        counter = 0
        print(left_array,right_array)
        while(left_pointer<len(left_array) and right_pointer <len(right_array)):
            if(left_array[left_pointer]<=right_array[right_pointer]):
                array[start+counter] = left_array[left_pointer]
                left_pointer+=1
            else:
                array[start+counter] = right_array[right_pointer]
                right_pointer+=1
            counter+=1
        while(left_pointer<len(left_array)):
            array[start+counter]=left_array[left_pointer]
            counter+=1
            left_pointer+=1
        while(right_pointer<len(right_array)):
            array[start+counter]=right_array[right_pointer]
            counter+=1
            right_pointer+=1
        return


        
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:] # Assigning all nums2 values to nums1
        self.mergeSort(nums1,0,m+n)
        
        