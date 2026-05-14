class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                st.append(ch)
            else:
                if len(st) == 0:
                    return False
                val = st.pop()
                if ch == ')' and  val != '(':
                    return False
                if ch == ']' and  val != '[':
                    return False
                if ch == '}' and  val != '{':
                    return False
            
        if len(st) == 0:
            return True
        return False


        
        