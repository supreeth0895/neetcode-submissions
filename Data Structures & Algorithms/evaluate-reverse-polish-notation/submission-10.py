class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t in "+-*/":
                print(s)
                b = s.pop()
                a = s.pop()
                if t == '+':
                    s.append(a+b)
                elif t == '-':
                    s.append(a-b)
                elif t == '*':
                    s.append(a*b)
                elif t == '/':
                    s.append(math.trunc(a/b))
            else:
                num = int(t)
                s.append(num) 
        return s.pop()