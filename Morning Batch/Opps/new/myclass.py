class Poly:
    """Hi i am a Polygon Class"""
    def __init__(self,no_of_sides=0):
        self.n = no_of_sides
        self.sides = [ 0 for var in range(no_of_sides) ]

    def set_Sides(self):
        n = self.n
        self.sides = []
        self.sides = [ float(input("Enter side{} : ".format(var))) for var in range(1,n+1) ]

    def get_Sides(self):
        n = self.n
        for var in range(1,n+1):
            print("Side{} = {}".format(var,self.sides[var-1]))


                
