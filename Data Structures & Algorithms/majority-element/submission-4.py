class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        maxnumber = -1
        length = len(nums)//2
        for number in nums:
            hashmap[number] = hashmap.get(number,0)+1
            if(hashmap[number]>length):
                maxnumber = number
        return maxnumber


        
        