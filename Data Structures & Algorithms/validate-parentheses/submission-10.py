class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {')':'(', '}':'{', ']':'['}
        stack = []
        i = 0
        while i < len(s):
            elem = s[i]
            if elem not in dict1.keys():
                stack.append(elem)
            else:
                if not stack:
                    return False
                if stack[-1] == dict1[elem]:
                    stack.pop()
                else:
                    return False
            i+=1
        return len(stack) == 0