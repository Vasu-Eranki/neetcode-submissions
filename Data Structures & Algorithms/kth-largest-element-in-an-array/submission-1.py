class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        diff = len(nums)-k
        for _ in range(diff):
            heapq.heappop(nums)
        return nums[0]