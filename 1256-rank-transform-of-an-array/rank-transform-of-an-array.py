class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ind = defaultdict(list)
        
        for i,x in enumerate(arr):
            ind[x].append(i)

        ind = dict(sorted(ind.items(),key=lambda x: x[0]))
        count=1
        for k,v in ind.items():
            for i in v:
                arr[i]=count
            count+=1
        
        return arr
        