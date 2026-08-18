class Solution:

    def encode(self, strs: List[str]) -> str:
        str1 = ""
        for item in strs:
            len1 = len(item)
            str1+=str(len1) + "#" + item
        return str1

    def decode(self, s: str) -> List[str]:
        len2 = len(s)
        if len2 == 0:
            return []
        k2 = 0
        str_len = ""
        while k2 < len2:
            if s[k2] != '#':
                str_len+=s[k2]
                k2 = k2 +1
            else:
                break
            str_len1 = int(str_len)
        index = k2
        b = []
        while index < len2:
            temp_str= ""
            j = index +1
            start_index = j
            for j in range(start_index, start_index + str_len1):
               temp_str+=s[j]
            b.append(temp_str)
            if str_len1 != 0:
              k1 = j+1
            else:
              k1 = j
            str_len = ""
            while k1 < len2:
                if s[k1] != '#':
                    str_len+=s[k1]
                    k1 = k1 +1
                else:
                    break
                str_len1 = int(str_len)
            index = k1
            
        return b
