class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #백트래킹 구현
        def dfs(index,path):
            #끝까지 탐색한 경우 종료
            if len(path)==len(digits):
                answer.append(path)
                return
            #현재 인덱스부터 탐색
            for i in range(index,len(digits)):
                #숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]:
                    dfs(i+1,path+j)
        #digits가 ""일 경우
        if not digits:
            return []

        dic={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno", "7":"pqrs", "8":"tuv","9":"wxyz"}
        answer=[]
        #백트래킹 실행
        dfs(0,"")

        return answer