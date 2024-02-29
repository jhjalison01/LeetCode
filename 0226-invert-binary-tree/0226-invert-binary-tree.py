# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            #해당 노드의 왼쪽 트리와 오른쪽 트리를 바꿈
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root #해당 노드를 리턴