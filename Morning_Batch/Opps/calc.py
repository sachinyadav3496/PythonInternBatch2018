class calc:
    def  __init__(self,x,y,z):
       self.x = x
       self.y = y
       self.z = z
    def add(self):
        return self.x+self.y+self.z
    def sub(self):
        return self.x-self.y-self.z
    def mul(self):
        return self.x*self.y*self.z

obj1 = calc(10,20,30)
obj2 = calc(30,20,10)

print(dir(obj1))
print("Add 1 = ",obj1.add())
print("Sub 1 = ",obj1.sub())
print("Mul 1 = ",obj1.mul())

print(dir(obj2))
print("Add 2 = ",obj2.add())
print("Sub 2 = ",obj2.sub())
print("Mul 2 = ",obj2.mul())

if dir(obj1) == dir(obj2) :
    print("Same objects")
    
