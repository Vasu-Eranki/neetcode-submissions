class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        # we know that len(s)>len(t)
        hashmap = {}
        for character in t:
            hashmap[character] = hashmap.get(character,0)+1
        hashmap_s = {}
        have = len(hashmap)
        need = 0 
        left_pointer = 0
        result = ""
        length_substring = float('inf')
        for right_pointer,character in enumerate(s):
            hashmap_s[character] = hashmap_s.get(character,0)+1
            if character in hashmap and hashmap_s[character]==hashmap[character]:
                need+=1
            if have==need:
                while(have==need): # slide left pointer over
                    if (right_pointer-left_pointer+1)<length_substring:
                        length_substring = (right_pointer-left_pointer+1)
                        result = s[left_pointer:right_pointer+1]
                    
                    left_character = s[left_pointer]
                    hashmap_s[left_character]-=1
                    left_pointer+=1
                    if left_character in hashmap and hashmap_s[left_character]<hashmap[left_character] :
                        need-=1

        return result if length_substring!=float('inf') else ""
        
        