class OddNumber:
    def __init__(self,m=0):
            self.m = m
            self.s = 1
    def __iter__(self):
        self.n = 1
        return self
    def __next__(self):
        v = self.n
        self.n += 2
        if self.s <= self.m : 
            self.s += 1
            return v
        else :
            raise StopIteration
        
