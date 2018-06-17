class Person :

    """ This is Person Class """

    def __init__(self,name,height,age,weight=None,blood_group=None):
        self.name = name
        self.height = height
        self.age = age
        self.weight = weight
        self.blood_group = blood_group
    def show(self):
        print("Name = {}".format(self.name))
        print("Age = {}".format(self.age))
        print("Weight = {}".format(self.weight))
        print("Height = {}".format(self.height))
        print("Blood Group = {}".format(self.blood_group))
    def change(self,name):
        self.name = name

person1 = Person('sachin',5.11,22,70,'B+')
person2 = Person('python',0,27,)

person1.show()
print()
person2.show()
print()
person1.change('hello')
person1.show()
person1.change('bye')
person2.show()
