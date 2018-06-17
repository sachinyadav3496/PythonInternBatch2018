import random 
class Grras :
    Institute_Name = 'Grras Solutions Private LTD.'
    Trainers = {
            'linux' : [ 'Rajat','Gaurav','Naveen' ],
            'python' : [ 'Sachin' ,'Rajat']
            }

    def __init__(self,st_name,st_fees,st_course):
        self.name = st_name
        self.fees = st_fees
        self.course = st_course
        self.trainer = random.choice(Grras.Trainers[st_course.lower()])
    def show(self):
        print("Student Name : ",self.name)
        print("Student Fees : ",self.fees)
        print("Student Course : ",self.course)
        print("Student Trainer : ",self.trainer)
        print("Institute : ",Grras.Institute_Name)
        print("All Trainers ",Grras.Trainers)

