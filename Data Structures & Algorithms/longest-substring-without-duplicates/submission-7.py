class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_len = len(s)
        if str_len == 0:
            return 0
        else:
            i =0
            j = 1
            uni_char = set()
            uni_char.add(s[i])
            while j < str_len:
                #print(f"Window: {i}: {j}: {uni_char}")
                if s[j] not in uni_char:
                    uni_char.add(s[j])
                    j+=1
                    #print(f"WIndow expanded: {j}: {uni_char}")
                else:
                    uni_char.remove(s[i])
                    i+=1
                    #print(f"Window shrinked: {i}: {uni_char}")
            return len(uni_char)