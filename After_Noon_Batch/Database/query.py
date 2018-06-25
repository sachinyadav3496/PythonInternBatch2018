import sqlite3 as sql

db = sql.connect('user.db')
c = db.cursor()

all_data = 'select * from student'

c.execute(all_data)
data = c.fetchall()

for var in data :
    print("ID : ",var[0])
    print("Name : ",var[1])
    print("Course : ",var[2])
    print("Fees : ",var[3])
    print("\n")


c.close()

db.close()
