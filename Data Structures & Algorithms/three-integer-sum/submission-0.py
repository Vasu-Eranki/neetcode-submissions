class Solution:
    def twoSum(self,nums:list[int],target:int)->list[int]:
        hashmap = {}
        results = []
        for num in nums:
            remainder = target - num
            if num in hashmap:
                results.append((hashmap[num],num))
            hashmap[remainder] = num
        return results
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        hashmap = {}
        sorted_nums = list(sorted(nums))
        for i in range(len(sorted_nums)):
            remainder = 0 - sorted_nums[i]
            list_expect_that_element =sorted_nums[i+1:]
            if(value:=self.twoSum(list_expect_that_element,remainder)):
                value = [(sorted_nums[i],)+j for j in value]
                for entry in value:
                    if(entry not in hashmap):
                        hashmap[entry] = True      
        return list(hashmap.keys())
        