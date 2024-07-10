# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        ans = []
        dq = deque()
        dq.append(root)
        while dq:
            node = dq.popleft()
            if node:
                ans.append(str(node.val))
                dq.append(node.left)
                dq.append(node.right)
            else:
                ans.append("")
        
        return ",".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        data = data.split(",")
        root = TreeNode(data[0])
        dq = deque()
        dq.append(root)
        i=1
        while dq:
            node = dq.popleft()
            if node:
                if i<len(data) and data[i]:
                    node.left = TreeNode(int(data[i]))
                    dq.append(node.left)
                i+=1
                if i<len(data) and data[i]:
                    node.right = TreeNode(int(data[i]))
                    dq.append(node.right)
                i+=1
        
        return root



        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))