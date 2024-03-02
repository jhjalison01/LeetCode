# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        answer=[]
        cnt=defaultdict(list)
        def solve(root, depth):
            nonlocal cnt
            if root is None:
                return
            cnt[depth].append(root.val) #깊이에 따라 숫자 저장
            solve(root.left,depth+1) #왼쪽 트리 탐색
            solve(root.right,depth+1) #오른쪽 트리 탐색
        #함수 실행
        solve(root,0)
        for i in cnt.keys():
            answer.append(sum(cnt[i])/len(cnt[i])) #깊이에 대한 평균값 저장
        return answer
