class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        count = {}
        for i, val in enumerate(nums):
            if val in count:
                return True
            else:
                count[val] = 1
        else:
            return False
        