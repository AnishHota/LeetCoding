class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ans = []

        def btrack(ind,curr):
            if ind==len(s) and len(curr)==4:
                self.ans.append(".".join(curr.copy()))
                return
            if len(curr)>=4:
                return
            for j in range(ind+1,min(ind+4,len(s)+1)):
                temp = s[ind:j]
                if temp.startswith("0") and len(temp)>1:
                    continue
                if 0<=int(s[ind:j])<=255:
                    curr.append(s[ind:j])
                    btrack(j,curr)
                    curr.pop()
            
        
        btrack(0,[])
        return self.ans