class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for elem in strs:
            encoded_str+=f"{len(elem)}#{elem}"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res
