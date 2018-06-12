class Poly:
    no_of_poly = 0
    """Hi i am a Polygon Class"""
    def __init__(self,name,no_of_sides=0):
        Poly.no_of_poly += 1
        self.name = name
        self.n = no_of_sides
        self.sides = [ 0 for var in range(no_of_sides) ]
    def set_Sides(self):
        n = self.n
        self.sides = []
        print("Enter Value of Sides for ",self.name)
        self.sides = [ float(input("Enter side{} : ".format(var))) for var in range(1,n+1) ]
    def get_Sides(self):
        print("Hi I am {} and I have My sides as :- ".format(self.name))
        n = self.n
        for var in range(1,n+1):
            print("Side{} = {}".format(var,self.sides[var-1]))
    def show_Obj(self):
        print("No of Polygons Till now is : ",Poly.no_of_poly)

triangle = Poly('Triangle',3)
rect = Poly('Rectangle',4)
triangle.set_Sides()
triangle.get_Sides()
rect.set_Sides()
rect.get_Sides()
hexs = Poly('Hexa',6)
hexs.show_Obj()

class Triangle(Poly):
    def __init__(self,name):
        Poly.__init__(self,name,3)
    def Area(self):
        a,b,c = self.sides
        s = (a+b+c) / 2
        from math import sqrt
        area  = sqrt(s*(s-a)*(s-b)*(s-c))
        return area
    
t1 = Triangle('Triangle1')
t2 = Triangle('Triangle2')
t1.set_Sides()
t2.set_Sides()
t1.get_Sides()
t2.get_Sides()
Area1 = t1.Area()
Area2 = t2.Area()
print("Area of Triangle one = %.2f \n Area of Triangle two is= %.2f"%(Area1,Area2))

