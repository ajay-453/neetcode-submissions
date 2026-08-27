class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        r = 0
        l = 0
        fd = {}
        wl = 0
        max_len = 0
        mf = 0
        ml = 0

        for r in range(len(s)):
            fd[s[r]] = fd.get(s[r], 0) + 1
            mf = max(mf, fd[s[r]])
            wl = r- l + 1
            if wl - mf > k:
                fd[s[l]]-=1
                l+=1
            ml = max(ml, r-l+1)
            r+=1
        return ml



            
