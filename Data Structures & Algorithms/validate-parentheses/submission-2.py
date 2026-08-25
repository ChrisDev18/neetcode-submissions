class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b in ("(", "{", "["):
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                
                p = stack.pop()
                
                if p == "(" and b != ")":
                    return False
                if p == "{" and b != "}":
                    return False
                if p == "[" and b != "]":
                    return False
    
        return len(stack) == 0