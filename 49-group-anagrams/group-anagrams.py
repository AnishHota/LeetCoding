class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for s in strs:
            arr = ''.join(sorted(s))
            dic[arr].append(s)

        result = []
        for x in dic.values():
            result.append(x)
        
        return result

        