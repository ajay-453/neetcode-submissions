class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1
        mid  = (l+r)//2
        if nums[l] < nums[mid]:
            l = mid
        else:
            r = mid
        while l<=r:
            mid = (l+r)//2
            if nums[mid] > nums[mid +1] :
                l = mid +1
            elif nums[mid] < nums[mid +1]:
                r = mid
            
            if l+1 == r:
                return min(nums[l], nums[r])
            elif l == r:
                return nums[l]

