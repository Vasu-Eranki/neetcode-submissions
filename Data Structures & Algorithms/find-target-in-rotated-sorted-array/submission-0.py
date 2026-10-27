class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for idx in range(len(nums)):
            if(nums[idx]==target):
                return idx
        return -1

        