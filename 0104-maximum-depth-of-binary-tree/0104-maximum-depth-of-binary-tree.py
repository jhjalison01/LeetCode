# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result=[]
        def dfs(current_node,depth):
            if current_node.left: #왼쪽 트리에 요소가 있을 경우
                dfs(current_node.left,depth+1) 
            if current_node.right: #오른쪽 트리에 요소가 있을 경우
                dfs(current_node.right,depth+1)
            #해당 노드가 리프 노드일 경우
            if current_node.left is None and current_node.right is None:
                result.append(depth) #깊이 저장
                return
        if root is None: #root 값이 없을 경우
            result.append(0) #깊이는 0
        else:
            dfs(root,1)
        return max(result) #최대 깊이 리턴
