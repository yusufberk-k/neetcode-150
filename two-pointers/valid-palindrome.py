# Valid Palindrome
# status: solo | retry: -
# note: forgot .lower() on comparison, 30 min lost; filtered into new string -> O(n) space, in-place skip gives O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear = ''
        for i in range(len(s)):
            if s[i].isalnum():
                clear += s[i]


        l = 0
        r = len(clear) - 1
        while (len(clear)//2 > l):
            if clear[l].lower() == clear[r].lower():
                l += 1
                r -= 1
                continue

            return False
        return True
