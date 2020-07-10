class EventSourcer():
    # Do not change the signature of any functions

    def _init_(self):
        self.value = 0
        self.list1 = [0]
        self.redo_item = 0
        
    def add(self, num: int):
        self.num = num
        self.value+=self.num
        self.list1.append(self.value)
        return self.value

    def subtract(self, num: int):
        self.num = num
        self.value-=self.num
        self.list1.append(self.value)
        return self.value

    def undo(self):
        self.redo_item = self.list1.pop()
        self.value = self.list1[-1]
        return self.value

    def redo(self):
        self.value = self.redo_item
        return self.value

    def bulk_undo(self, steps: int):
        for i in range(0,steps):
            self.redo_item = self.list1.pop()
        self.value = self.list1[-1]
        return self.value

    def bulk_redo(self, steps: int):
        pass
