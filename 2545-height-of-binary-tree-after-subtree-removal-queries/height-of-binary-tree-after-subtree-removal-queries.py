# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depth_map = defaultdict(lambda: (-1,-1,0))
        level_map = defaultdict(list)
        def dfs(root,level):
            if not root:
                return 0
            
            depth = max(dfs(root.left,level+1), dfs(root.right,level+1))
            level_map[root.val] = [level,depth]
            m,sm,size = depth_map[level]
            if depth>=m:
                depth_map[level] = (depth,m,size+1)
            elif depth>sm:
                depth_map[level] = (m,depth,size+1)
            else:
                depth_map[level] = (m,sm,size+1)

            return depth+1
        
        dfs(root,0)
        ans = []

        for q in queries:
            level,depth = level_map[q]
            m,sm,size = depth_map[level]
            if size==1:
                ans.append(level-1)
                continue
            elif depth==m:
                ans.append(sm+level)
            else:
                ans.append(m+level)

        return ans
        