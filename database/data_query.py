import sqlite3 as sql
def query():
    try : 
        db = sql.connect('st_data.db')
        c = db.cursor()
    except Exception as error :
        print("!!ERROR!!",error)
        exit(0)
    
    print("\t1.Show All Data\n\t2.Query with id\n\t3.Query with fees")
    ch = int(input("\tChoice : "))
    if ch == 1 :
        cmd = "select * from student"
        #Query to fetch all data from table
        c.execute(cmd)
        data = c.fetchall()
        print("{:>15}{:>15}{:>30}{:>15}{:>30}{:>30}".format("Name","ID","Course","Fees","Ph_no","Email"))
        for d in data:
            print("{:>15}{:>15}{:>30}{:>15}{:>30}{:>30}".format(*d))
    elif ch == 2 :
        sid = int(input("\tEnter Id : "))
        c.execute("select * from student where id={}".format(sid))
        data = c.fetchone()
        print("{:>15}{:>15}{:>30}{:>15}{:>30}{:>30}".format("Name","ID","Course","Fees","Ph_no","Email"))
        print("{:>15}{:>15}{:>30}{:>15}{:>30}{:>30}".format(*data))

    elif ch == 3 :
        pass
    else :
        print("Wrong Choice")
query()
