class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        val = 0
        for val in range(len(s)):
            if s[val].isalnum():
                s1 = s1 + s[val]
        left = 0
        right = len(s1) - 1
        while left <= right:
            if s1[left].lower() == s1[right].lower():
                left = left + 1
                right = right - 1
            else:
                return False
        if left > right:
            return True