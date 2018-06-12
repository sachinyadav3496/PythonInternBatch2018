import sqlite3 as sql
db = sql.connect('st_data.db')
c = db.cursor()
#To create a table
#create table table_name ( col1_name data type, col2_name data type .....)
print("Creating Table Student into st_data.db database")
cmd = "create table student(name varchar(50) not null,\
id int(6) primary key ,course varchar(500) not null ,fees float NOT NULL ,ph_no varchar(20) NOT NULL ,\
email varchar(100) )"
c.execute(cmd)
db.commit()
c.close()
db.close()

