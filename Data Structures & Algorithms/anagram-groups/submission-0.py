class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = {}
        sorted_str = [(i,"".join(sorted(i)))for i in strs]
        sorted_str = list(sorted(sorted_str,key=lambda x:x[1]))
        for key,value in sorted_str:
            if value in hashmap:
                hashmap[value].append(key)
            else:
                hashmap[value]=[key]
        return list(hashmap.values())
                     