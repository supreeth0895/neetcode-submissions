#SUPREETH
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for ch in s:
            if (ord(ch) >= ord('A') and ord(ch) <= ord('Z')):
                new_str = new_str + chr(ord(ch)-ord('A')+ord('a'))
            elif (ord(ch) >= ord('a') and ord(ch) <= ord('z')) or \
                (ord(ch) >= ord('0') and ord(ch) <= ord('9')) :
                new_str = new_str + ch


                

        start = 0
        end = len(new_str)-1
        for i in range(start,end//2+1):
            if new_str[i] != new_str[end-i]:
                return False
        return True

        