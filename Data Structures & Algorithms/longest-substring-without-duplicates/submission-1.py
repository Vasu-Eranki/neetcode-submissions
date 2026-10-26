class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==1):
            return 1
        hashmap = {}
        left_pointer = 0
        right_pointer = 0
        max_value = right_pointer - left_pointer
        while(right_pointer<len(s)):
            character = s[right_pointer]
            if character not in hashmap:
                hashmap[character]=True
                right_pointer+=1
            else:
                first_character = s[left_pointer]
                del hashmap[first_character]
                left_pointer+=1
            max_value = max(max_value,right_pointer-left_pointer)
        return max_value




            

