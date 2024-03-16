class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer=[]
        #elements: 원소들, index: 현재 원소의 인덱스 값, cnt: 원소들의 합
        def dfs(elements,index,cnt):
            #종료 조건
            #타깃 값에 도달했을 때
            if cnt==0:
                answer.append(elements[:])
                return
            #타깃 값보다 합이 클 때
            if cnt<0:
                return
            #자신부터 나머지 원소 탐색
            for i in range(index,len(candidates)):
                dfs(elements+[candidates[i]],i,cnt-candidates[i])

        dfs([], 0, target)
        return answer