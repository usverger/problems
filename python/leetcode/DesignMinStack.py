from typing import List

class MinStack:

    def __init__(self):
        self.l = []
        
    def push(self, x: int) -> None:
        if self.l:
            m = self.l[-1][1]
            self.l.append([x, min(x,m)])
        else:
            self.l.append([x, x])

    def pop(self) -> None:
        self.l.pop()

    def top(self) -> int:
        return self.l[-1][0]

    def getMin(self) -> int:
        return self.l[-1][1]