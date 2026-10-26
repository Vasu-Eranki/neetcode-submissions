class Solution:
    def euclideanDistance(self,point:List[List[int]]):
        sum_of_squares = point[0]**2+point[1]**2
        return sum_of_squares**(0.5)
    def mergeSort(self,array:List[List[int]],start:int,end:int)->None:
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
            if(self.euclideanDistance(left_array[left_counter])<=self.euclideanDistance(right_array[right_counter])):
                array[start+counter] = left_array[left_counter]
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

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.mergeSort(points,0,len(points))
        return points[:k]