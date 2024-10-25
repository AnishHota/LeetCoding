class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        fset = set()
        folder.sort()
        ans = []
        for x in folder:
            fname = x.split("/")
            curr = ""
            for f in fname:
                curr += "#" + f
                if curr in fset:
                    curr = ""
                    break
            if curr != "":
                fset.add(curr)
                ans.append(x)
        return ans