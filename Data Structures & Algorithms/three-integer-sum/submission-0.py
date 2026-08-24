class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
 
        list1 = sorted(nums)
        len1 = len(list1)
        result = []
        for i in range(len1-2):
            j = i + 1
            k = len1 -1
            if i > 0 and list1[i] == list1[i-1]:
                #This is to avoid the recalculation
                #Just skip the duplicates until the last instance
                i = i + 1
            else:
                while j < k:
                    
                    sum1 = list1[i] + list1[j] + list1[k] 
                    if sum1 == 0:
                        triplet = [list1[i], list1[j], list1[k]]
                        result.append(triplet)
                        #Result recorded
                        if list1[j] != list1[j+1]:
                          j = j + 1
                          #Move next when adjacent elements are not same
                        else:
                            while j < k  and list1[j] == list1[j+1]:
                                #If adjacent elements are same, then pass through the list
                                j = j+ 1 # this will be last same element (moving right)
                            j = j + 1 # this is next different element

                        if list1[k] != list1[k-1]:
                           k = k -1
                        else:
                            while k > 1 and list1[k] ==list1[k-1]:
                                #If adjacent elements are same, then pass through the list
                                k = k -1 # this will be first same element (moving left)
                            k = k - 1 # this is next different element

                    elif sum1 > 0:
                        k = k -1 # Here we need to get close to ZERO, if the right most element give the +ive output, then we need to move in descending order
                    elif sum1 < 0:
                        j = j + 1# Here we need to get close to ZERO, if the left most element give the -ive output, then we need to move in Ascending order

        return result

                