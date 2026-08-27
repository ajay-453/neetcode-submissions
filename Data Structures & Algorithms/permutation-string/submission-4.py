class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        l1 = len(s1)
        l2 = len(s2)
        us1 = {}
        result = []
        for val in s1:
            us1[val] = us1.get(val, 0) + 1

        while r < l2 - l1 + 1:
            s3 = s2[l:r+l1]
            us2 = {}
            for val in s3:
              us2[val] = us2.get(val, 0) + 1
            if us2 == us1:
                result.append(s3)
            l+=1
            r+=1
        if result:
            return True
        else:
            return False
                