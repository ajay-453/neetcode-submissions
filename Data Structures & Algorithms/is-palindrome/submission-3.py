class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left <= right:

            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() == s[right].lower():
                    left = left + 1
                    right = right - 1
                else:
                    return False
            elif left <= right and not s[left].isalnum():
                left = left +1
            elif left <= right and not s[right].isalnum():
                right = right - 1
        if left > right:
            return True
