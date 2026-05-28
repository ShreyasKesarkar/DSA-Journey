class MaxStack:

    def __init__(self):
        self.stack = []
        self.max = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.max:
            if val >= self.max[-1]:
               self.max.append(val)
        else:
            self.max.append(val)   


    def pop(self) -> None:
        if self.stack[-1] == self.max[-1]:
            self.max.pop()
        self.stack.pop()    


        

    def top(self) -> int:
        return self.stack[-1]

    def getMax(self) -> int:
        return self.max[-1]