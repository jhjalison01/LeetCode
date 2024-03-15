class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer=[]
        #백트래킹 구현
        def dfs(elements, num):
            if len(elements)==k: #k개 요소가 들어있는 경우
                answer.append(elements[:]) #정답 리스트에 저장
                return

            for i in range(num,n+1):
                elements.append(i) #해당 숫자 삽입
                dfs(elements,i+1) #다음 숫자 탐색
                elements.pop()
        dfs([],1)
        return answer