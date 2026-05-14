class MinStack:

    def __init__(self):
        self.st1 = []
        self.st2 = []

        

    def push(self, val: int) -> None:
        self.st1.append(val)
        if len(self.st2) == 0:
            self.st2.append(val)
        else:
            self.st2.append(min(self.st2[len(self.st2)-1],val))


        

    def pop(self) -> None:
        self.st1.pop()
        self.st2.pop()
        

    def top(self) -> int:
        return self.st1[len(self.st1)-1]
        

    def getMin(self) -> int:
        return self.st2[len(self.st2)-1]

        



#HINT: Instead of searching the whole stack to find the minimum every time, we can keep a second stack that always stores the minimum value up to that point.