class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i,j = 0,len(skill)-1
        curr = skill[i]+skill[j]
        res = 0
        while i<=j:
            if curr!=skill[i]+skill[j]:
                return -1
            res += skill[i]*skill[j]
            i+=1
            j-=1
        return res