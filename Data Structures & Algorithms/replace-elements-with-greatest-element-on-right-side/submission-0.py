class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_element_so_far = arr[-1]
        for i in range(len(arr)-1,-1,-1):
            value = arr[i]
            arr[i] = max_element_so_far
            max_element_so_far = max(value,max_element_so_far)
        arr[-1]=-1
        return arr
        