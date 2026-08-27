class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_len = len(s)
        i =0
        j = 1
        uni_char = []
        max_sub_str = ""
        uni_char.append(s[i])
        while j < str_len:
            if s[j] not in uni_char:
                uni_char.append(s[j])
                print(s[j])
                j+=1
                print(f"{i}:{j}:{uni_char}")
            else:
                sub_str = s[i:j]
                print(sub_str)
                uni_char = []
                if len(sub_str) > len(max_sub_str):
                    max_sub_str = sub_str
                    print(f"max:{max_sub_str}")
                i = j
                uni_char.append(s[i])
                j+=1
                print(f"{i}:{j}:{uni_char}")
        return len(max_sub_str)