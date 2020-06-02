#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# O(h) and O(h)
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def dfs(node):
            if not node:
                return None
            if node.val > key:
                node.left = dfs(node.left)
                return node
            elif node.val < key:
                node.right = dfs(node.right)
                return node
            else:
                if not node.left or not node.right:
                    return node.left or node.right
                curr = node.right
                while curr.left:
                    curr = curr.left
                curr.left = node.left
                return node.right

        root = dfs(root)
        return root


# O(h) and O(h)
class Solution:
    def successor(self, root):
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root
# @lc code=end

