class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        hashmap = {}
        def dp(index):
            if index==len(s):
                return [""]
            if index in hashmap:
                return hashmap[index]
            res = []            
            for word in wordDict:
                substring = s[index:]
                if substring.startswith(word):
                    suffixes_that_can_be_built:List[str] = dp(index+len(word))
                    for suffx in suffixes_that_can_be_built:
                        res.append(word+(" "+suffx if suffx else ""))
            hashmap[index]=res
            return hashmap[index]
        dp(0)
        return hashmap[0]
            
        
        