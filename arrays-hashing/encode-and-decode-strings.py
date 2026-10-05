# Encode and Decode Strings
# status: solo | retry: -
# note: retry passed, remembered the idea but implementation took far too long; could be more pythonic

class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for w in strs:
            st += str(len(w)) + '!' + w
        return st

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        b = 0
        while i < len(s):
            w = ""
            if s[i] == '!':
                l = int(''.join(s[b:i]))
                for j in range(1, l+1):
                    w += s[i+j]
                b = i + l + 1
                strs.append(w)
                i += l+1
            
            else: i+=1

        return strs
