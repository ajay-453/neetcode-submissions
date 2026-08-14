class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency_dict = {}
        for num in nums:
            if num not in frequency_dict:
                frequency_dict[num] = 1
            else:
                frequency_dict[num]+=1
        
        unique_keys = list(frequency_dict.keys())

        unique_keys.sort(key=lambda x: (-frequency_dict[x], x))

        return unique_keys[:k]