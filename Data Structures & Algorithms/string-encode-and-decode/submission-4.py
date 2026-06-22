class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for idx, elem in enumerate(strs):
            res += str(len(elem)) +"#" +elem
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j]!='#':
                j+=1
            len1 = int(s[i:j])
            i = j+1
            j = j+1+len1
            res.append(s[i:j])
            i=j
        return res