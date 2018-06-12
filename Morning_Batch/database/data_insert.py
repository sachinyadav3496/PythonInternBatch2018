import sqlite3 as sql
#connect your data base 
db = sql.connect('st_data.db')
c = db.cursor()

while input("Press something to add values in table : "):
    cmd = "insert into student values('{0}',{1},'{2}',{3},'{4}','{5}')"
    name = input("Enter name : ")
    sid = int(input("Enter id : "))
    crs = input("Course : ")
    fees = float(input("Fees : "))
    ph = input("Enter phone Number : ")
    email = input("Email : ")
    cmd = cmd.format(name,sid,crs,fees,ph,email)
    c.execute(cmd)
    db.commit()
c.close()
db.close()

