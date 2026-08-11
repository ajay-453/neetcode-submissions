class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = list(s)
        t1 = list(t)
        d1 = {}
        d2 = {}
        if len(s1) != len(t1):
            return False
        else:
            for i in range(len(s1)):
                if s1[i] not in d1:
                    d1[s1[i]] = 1
                else:
                    d1[s1[i]]+=1
            for i in range(len(t1)):
                if t1[i] not in d2:
                    d2[t1[i]] = 1
                else:
                    d2[t1[i]]+=1
            print(d1)
            print(d2)
            if d1 == d2:
                return True
            return False
                
            



        