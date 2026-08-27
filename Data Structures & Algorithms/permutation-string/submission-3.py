class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        l1 = len(s1)
        l2 = len(s2)
        us1 = set()
        result = []
        for val in s1:
           us1.add(val)
        while r < l2 - l1 + 1:
            s3 = s2[l:r+l1]
            us2 = set()
            for val in s3:
              if val in us1:
                us2.add(val)
            if len(us2) == l1:
                result.append(s3)
            l+=1
            r+=1
        if result:
            return True
        else:
            return False
                