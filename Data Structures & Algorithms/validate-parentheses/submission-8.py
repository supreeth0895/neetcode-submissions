class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {')':'(', '}':'{', ']':'['}
        stack = []
        for elem in s:
            if elem not in dict1.keys():
                stack.append(elem)
            else:
                if not stack:
                    return False
                if stack[-1] == dict1[elem]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0