class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for elem in tokens:
            if elem not in ['+', '-', '*', '/']:
                stack.append(elem)
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                if elem == '+':
                    final_val = int(val1) + int(val2)
                elif elem == '-':
                    final_val = int(val2) - int(val1)
                elif elem == '*':
                    final_val =int(val1) * int(val2)
                else:
                    final_val = int(val2) / int(val1)
                stack.append(final_val)
        return int(stack[0])