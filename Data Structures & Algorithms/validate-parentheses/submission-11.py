class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {')':'(', '}':'{', ']':'['}
        stack = []
        i = 0
        while i < len(s):
            if s[i] not in dict1.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if stack[-1] == dict1[s[i]]:
                    stack.pop()
                else:
                    return False
            i+=1
        return len(stack) == 0