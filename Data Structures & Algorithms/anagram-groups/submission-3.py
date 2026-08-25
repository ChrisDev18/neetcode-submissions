class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        
        anagrams_strs = {}

        for string in strs:
            each_count = str(sorted(string))
            if each_count in anagrams_strs:
                anagrams_strs[each_count].append(string)
            else:
                anagrams_strs[each_count] = [string]
        
        return list(anagrams_strs.values())

