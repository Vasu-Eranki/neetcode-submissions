class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        stack = [nums[0]]
        max_sequence = 1
        print(nums)
        for idx in range(1,len(nums)):
            if nums[idx]==(stack[-1]+1):
                stack.append(nums[idx])
            else:
                while(stack and (stack[-1]+1)<nums[idx]):
                    stack.pop()
                if stack:
                    if nums[idx]==(stack[-1]+1):
                        stack.append(nums[idx])
                else:
                    stack.append(nums[idx])
            max_sequence = max(max_sequence,len(stack))
        return max_sequence

                