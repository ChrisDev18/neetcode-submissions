class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # is an anagram if they contain the same letters
        if len(s) != len(t):
            return False
        
        counter = {}
        for i in range(len(s)):
            each_s = s[i]
            each_t = t[i]
            if each_s in counter:
                counter[each_s] += 1
            else:
                counter[each_s] = 1
            
            if each_t in counter:
                counter[each_t] -= 1
            else:
                counter[each_t] = -1
        
        for value in counter.values():
            if value != 0:
                return False
        
        return True