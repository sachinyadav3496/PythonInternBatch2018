class student:
    nst = 0
    def __init__(self,name,m1,m2,m3):
        student.nst += 1
        self.name = name
        self.addr = None
        self.fname = None
        self.mname = None
        self.email = None
        self.ph_no = None
        self.sub1 = m1
        self.sub2 = m2
        self.sub3 = m3
    def show(self):
        print("Sub1 = ",self.sub1)
        print("Sub2 = ",self.sub2)
        print("Sub2 = ",self.sub3)
    def update_marks(self,m1,m2,m3):
        self.sub1 = m1
        self.sub2 = m2
        self.sub3 = m3
    def get_details(self,email,address,fname,mname,ph_no):
        self.email = email
        self.addr = address
        self.fname = fname
        self.mname = mname
        self.ph_no = ph_no
    def __del__(self):
        del self

