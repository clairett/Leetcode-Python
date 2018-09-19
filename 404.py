# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)



        # iterative
        # result = 0
        # if not root: return result
        # stack = [(root, 0)]
        # while stack:
        #     node, num = stack.pop()
        #     if num < 0 and node.left == None and node.right == None:
        #         result += node.val
        #     if node.left:
        #         stack.append([node.left, -1])
        #     if node.right:
        #         stack.append([node.right, 1])
        # return result