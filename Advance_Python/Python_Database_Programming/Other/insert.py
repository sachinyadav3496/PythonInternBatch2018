import sqlite3 as sql

db = sql.connect('user.db')
c = db.cursor()

while True :
    Id = int(input("Enter id of student : "))
    Name = input("Enter name of the student : ")
    Course = input("Enter Course detail : ")
    Fees = float(input("Fees : "))

    cmd = "insert into student values({},'{}','{}',{})".format(Id,Name,Course,Fees)
    c.execute(cmd)
    db.commit()
    print("\nStudent Added Sucessfully")

    ch = input("\nPress y to add more : ").strip().lower()
    if not( ch == 'y' or ch == 'yes' ) :
        break

c.close()
db.close()
