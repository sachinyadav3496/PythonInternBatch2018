from class4 import student

class grade(student):
    def __init__(self,name,m1,m2,m3):
        student.__init__(self,name,m1,m2,m3)
    def st_grade(self):
        g = ( (self.sub1 + self.sub2 + self.sub3) / 300 ) * 100 
        if g >= 75 :
            self.g = 'A'
        elif g >= 60 :
            self.g = 'B'
        elif g >= 33 :
            self.g = 'C'
        else :
            self.g = 'FAIL'
    def common(self):
        print("Name = ",self.name)
        print("Father Name = ",self.fname)
        print("Mother Name = ",self.mname)
        print("Phone Number = ",self.ph_no)
        print("Email = ",self.email)
        print("Address = ",self.addr)
    def show(self):
        grade.common(self)
        student.show(self)
        print("Grade : ",self.g)

    def __str__(self):
        return "Hi my name is {} and i am an object of grade class".format(self.name)
