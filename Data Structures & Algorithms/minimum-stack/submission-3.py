#SUPREETH
class MinStack:

    def __init__(self):
        self.st1 = []
        self.st2 = []
        self.size = 0

        

    def push(self, val: int) -> None:
        self.st1.append(val)
        if self.size == 0:
            self.st2.append(val)
        else:
            self.st2.append(min(self.st2[(self.size)-1],val))
        self.size = self.size + 1


        

    def pop(self) -> None:
        self.st1.pop()
        self.st2.pop()
        self.size = self.size-1
        

    def top(self) -> int:
        return self.st1[self.size-1]
        

    def getMin(self) -> int:
        return self.st2[self.size-1]

        



#HINT: Instead of searching the whole stack to find the minimum every time, we can keep a second stack that always stores the minimum value up to that point.