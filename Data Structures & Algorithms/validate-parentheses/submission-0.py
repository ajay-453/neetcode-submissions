class Solution:
    def isValid(self, s: str) -> bool:

        pair  = {'}': '{', ']': '[', ')': '('}
        stack = []
        for val in s:
            if val not in pair:
                stack.append(val)
            elif val in pair and stack[-1] == pair[val]:
                stack.pop()
        if stack:
            return False
        else:
            return True
        

        