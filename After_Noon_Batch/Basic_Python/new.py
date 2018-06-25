class infinte:
    def __iter__(self,):
        self.eve,self.odd = 0,-1
        return self
    def __next__(self,):
        self.eve+=2;self.odd+=2
        return self.odd,self.eve
k = iter(infinte())
while True :
    print("{0:15}{1:15}{0:15}{1:15}".format(*next(k)))
print("Hello World")
