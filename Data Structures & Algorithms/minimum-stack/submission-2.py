class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        val_min = min(val, self.min_stack[-1]) if self.min_stack else val
        if self.min_stack and val_min != self.min_stack[-1]:
            self.min_stack.append(val_min) 
        elif not self.min_stack:
             self.min_stack.append(val_min) 
            


        return None

    def pop(self) -> None:
        val = self.stack.pop()
        if self.min_stack[-1] == val:
            self.min_stack.pop()
        return None
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]

        
    

input = ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
output  = []

min_stack = MinStack()
output.append("null")
i =1
while i < len(input):
    if input[i] == "push":
        min_stack.push(input[i+1])
        i+=1
        output.append("null")
        output.append("null")
    elif input[i] == "pop":
        min_stack.pop()
        output.append("null")
    elif input[i] == "top":
        val = min_stack.top()
        output.append(val)
    else:
        val = min_stack.getMin()
        output.append(val)
    i+=1



    