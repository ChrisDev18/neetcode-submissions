class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_clean = ''.join([char.lower() for char in s if char.isalnum()])

        p1 = 0
        p2 = len(str_clean) - 1

        while p1 < p2:
            if str_clean[p1] != str_clean[p2]:
                return False

            p1 += 1
            p2 -= 1
        
        return True