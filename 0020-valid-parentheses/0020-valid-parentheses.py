class Solution:
    def isValid(self, s: str) -> bool:
        data=dict(('()','[]','{}'))
        stack=[]

        for c in s:
            if c in '([{':
                stack.append(c)
            #c가 ),},]인 경우 stack에 그에 대응하는 (,{,[가 필요, 만약 없다면 false 리턴
            elif len(stack) == 0 or c!=data[stack.pop()]:
                return False
        #stack이 비었을 경우 true, stack에 무언가 남아 있다면 false 리턴
        return len(stack)==0