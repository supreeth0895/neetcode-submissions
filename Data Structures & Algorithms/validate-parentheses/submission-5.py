class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {')':'(', '}':'{', ']':'['}
        stack = []
        for elem in s:
            if elem in dict1.values():
                stack.append(elem)
            elif elem in dict1.keys():
                if stack and stack[-1] == dict1[elem]:
                    stack.pop()
                else:
                    return False
        return False if stack else True