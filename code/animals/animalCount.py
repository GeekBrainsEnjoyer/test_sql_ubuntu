

class AnimalCount:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

    def delt(self):
        self.count -= 1

    def getCount(self):
        return self.count
    
    def setCount(self, new_count):
        self.count = new_count

