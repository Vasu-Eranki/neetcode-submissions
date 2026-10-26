class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if (k==0):
            return
        start_index = len(nums)-k
        nums[:] = nums[start_index:]+nums[:start_index]

