class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_length = min([len(s) for s in strs])
        prefix_to_check = ""
        for i in range(0,common_length,1):
            prefix_to_check += strs[0][i]
            for idx in range(1,len(strs)):
                substr = strs[idx][:i+1]
                if(substr!=prefix_to_check):
                    return prefix_to_check[:-1]
        return prefix_to_check