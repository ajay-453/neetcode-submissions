class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        nums_set = set(nums)
        for num in nums_set:
            print(num)
            if num -1 not in nums_set:
                index = 1
                while True:
                    if num + index in nums_set:
                        index+=1
                    else:
                        if index > max_count:
                            max_count = index
                        break
        return max_count
            