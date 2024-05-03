class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        version1_list = list(map(int,version1.split(".")))
        version2_list = list(map(int,version2.split(".")))

        version1_list

        v1_len = len(version1_list)
        v2_len = len(version2_list)

        if v1_len<v2_len:
            version1_list += [0]*(v2_len-v1_len)
        else:
            version2_list += [0]*(v1_len-v2_len)

        n = max(v1_len,v2_len)
        
        for i in range(n):
            if version1_list[i]>version2_list[i]:
                return 1
            elif version1_list[i]<version2_list[i]:
                return -1
        
        return 0