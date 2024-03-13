class Solution:
    def pivotInteger(self, n: int) -> int:
        arr = [x for x in range(1,n+1)]
        pre = [0 for _ in range(n)]
        post = [0 for _ in range(n)]
        for i in range(n):
            pre[i]=arr[i]+pre[i-1]
            post[i]=arr[n-1-i]+post[i-1]
        ind = 0
        for x,y in zip(pre,sorted(post,reverse=True)):
            ind+=1
            if x==y:
                return ind
        return -1
        