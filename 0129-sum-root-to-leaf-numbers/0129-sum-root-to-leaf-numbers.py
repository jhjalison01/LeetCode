# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result=[] #숫자 저장할 리스트
        def solve(root,num):
            nonlocal result
            if root is None:
                return
            num+=str(root.val) #해당 노드의 숫자 추가
            #해당 노드가 리프 노드일 경우
            if root.left is None and root.right is None:
                result.append(int(num)) #숫자 저장
                return
            solve(root.left,num) #왼쪽 트리 탐색
            solve(root.right,num) #오른쪽 트리 탐색
        solve(root,"")
        return sum(result)
            