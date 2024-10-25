class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = [folder[0]]
        for x in folder[1:]:
            if not x.startswith(ans[-1]+"/"):
                ans.append(x)
        return ans