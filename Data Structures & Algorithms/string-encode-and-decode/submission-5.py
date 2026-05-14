class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str =""
        for st in strs:
            size = len(st)
            prefix = str(size) + "#"
            encoded_str = encoded_str+prefix+st
        print(encoded_str)
        return encoded_str


    def decode(self, s: str) -> List[str]:
        ans = []
        word = ""
        size_known = False
        size_str =""
        i=0
        while i < len(s):
            ch = s[i]
            if  ch == '#':
                size_known = True
                print(size_str)
                size = int(size_str)
                size_str = ""
                word = s[i+1:i+size+1]
                ans.append(word)
                word =""
                i = i+size+1
            else:
                size_str = size_str+ch
                i = i+1
        return ans