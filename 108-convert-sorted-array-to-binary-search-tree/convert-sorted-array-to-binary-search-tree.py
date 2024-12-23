# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def div(l,r):

            if l>r:
                return None

            mid = int(l+(r-l)//2)
            temp = TreeNode(nums[mid])
            temp.left = div(l,mid-1)
            temp.right = div(mid+1,r)
            return temp
        
        return div(0,len(nums)-1)
            