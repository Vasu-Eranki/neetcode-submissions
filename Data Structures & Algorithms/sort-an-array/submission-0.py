class Solution:
    def mergeSort(self,array,start,end):
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
        while(left_counter<len(left_array) and right_counter<len(right_array)):
            if(left_array[left_counter]<=right_array[right_counter]):
                array[start+counter]=left_array[left_counter]
                left_counter+=1
            else:
                array[start+counter] = right_array[right_counter]
                right_counter+=1
            counter+=1
        while(left_counter<len(left_array)):
            array[start+counter] = left_array[left_counter]
            left_counter+=1
            counter+=1
        while(right_counter<len(right_array)):
            array[start+counter] = right_array[right_counter]
            right_counter+=1
            counter+=1
        return
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums,0,len(nums))
        return nums

        