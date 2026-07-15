class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[' :
                res.append(ch)
            else :
                if ch == ')' and res and res[-1] == '(':
                    res.pop()
                elif ch == '}' and res and res[-1] == '{':
                    res.pop()
                elif ch == ']' and res and res[-1] == '[':
                    res.pop()
                else :
                    return False
        return True if len(res) == 0 else False
        