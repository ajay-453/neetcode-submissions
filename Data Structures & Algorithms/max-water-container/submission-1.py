class Solution:
    def maxArea(self, heights: List[int]) -> int:
        list_len = len(heights)
        small_index = 0
        large_index = list_len -1 
        max_area = 0
        area = lambda small_index, large_index: (large_index - small_index) * min (heights[small_index], heights[large_index])
        while small_index <= large_index:
            area_val = area(small_index, large_index)
            if heights[small_index] <= heights[large_index]:
                small_index = small_index + 1
            elif heights[small_index] > heights[large_index]:
                large_index = large_index - 1
            
            if area_val > max_area:
                  max_area = area_val
        return max_area