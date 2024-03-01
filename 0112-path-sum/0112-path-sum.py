# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, targetSum, curr):
            if root:
                curr+=root.val #현재 노드 값 더하기
                #타깃값에 도달하고 현재 노드가 리프 노드일 경우
                if curr==targetSum and root.left==None and root.right==None:
                    return True #true 리턴
                return dfs(root.left,targetSum,curr) or dfs(root.right,targetSum,curr)
        return dfs(root, targetSum, 0)