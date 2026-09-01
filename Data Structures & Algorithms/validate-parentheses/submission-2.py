class Solution:
    def isValid(self, s: str) -> bool:

        pair  = {'}': '{', ']': '[', ')': '('}
        stack = []
        for val in s:
            if val not in pair:
                stack.append(val)
            elif stack and stack[-1] == pair[val]:
                stack.pop()
            else:
                stack.append(val)
        if stack:
            return False
        else:
            return True
        

        