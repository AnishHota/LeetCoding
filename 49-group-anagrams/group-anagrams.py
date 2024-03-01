class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for s in strs:
            arr = [-1 for _ in range(27)]
            for c in s:
                arr[ord(c)-97]+=1
            temp = ''.join([str(elem) for elem in arr])
            dic[temp].append(s)

        result = []
        for x in dic.values():
            result.append(x)
        
        return result

        