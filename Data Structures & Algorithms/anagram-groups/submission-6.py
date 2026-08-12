class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for item in strs:
            val = "".join(sorted(item))
            if val not in dict1:
                dict1[val] = [item]
            else:
                temp_list = dict1[val]
                temp_list.append(item)
                dict1[val] = temp_list
        return list(dict1.values())