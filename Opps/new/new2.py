class one:
    "This is class one."
    pvar = "Public Variable" #class variable
    _prvar = "Protected Variable" #clas Variable
    __privar = "Private Variable" #class Variable
    def __init__(self,x,y):
        self.x = x #object variable
        self.y = y #object attribute
    def show(self):
        print("Objects Attributes are : (self variables)")
        print("Name : ",self.x)
        print("Type : ",self.y)
    def class_show(self):
        print("Class Attributes are : (Common or Share Variables)")
        print("Public Variable = ",one.pvar)
        print("Protect Variable = ",one._prvar)
        print("Private Variable = ",one.__privar)
        
    def set_val(self):
        self.x = input("New Value for X : ")
        self.y = input("New Value for y : ")
    def set_class(self):
        one.pvar = input("New Public Var : ")
        one._prvar = input("New Protect Var : ")
        one.__privar = input("New Private VAr : ")
        

