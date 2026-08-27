class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        l1 = len(s1)
        l2 = len(s2)
        us1 = {}
        for val in s1:
            us1[val] = us1.get(val, 0) + 1
        print(us1)
        us2 = {}
        for i  in range(len(s2)): 
            us2[s2[i]] = us2.get(s2[i], 0) + 1
            if i >= l1:
                print(us2)
                lc = s2[i-l1]
                us2[lc]-=1
                if us2[lc] == 0:
                    del us2[lc]
            if us1 == us2:
              return True
        return False

