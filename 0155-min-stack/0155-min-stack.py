class MinStack:

    def __init__(self):
        self.stack=[] #일반 스택
        self.stack_min=[] #최소값 스택
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack_min)==0: #최소값 스택이 비어있을 경우
            self.stack_min.append(val) #요소 추가
        else:
            #가장 상단의 값과 현재 값 중 최소값 추가
            self.stack_min.append(min(self.stack_min[-1],val))
        
    def pop(self) -> None:
        #일반 스택, 최소값 스택 모두 pop
        self.stack.pop() 
        self.stack_min.pop()

    def top(self) -> int:
        #일반 스택 상단 값 리턴
        return self.stack[-1]

    def getMin(self) -> int:
        #최소값 스택 상단 값 리턴
        return self.stack_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()