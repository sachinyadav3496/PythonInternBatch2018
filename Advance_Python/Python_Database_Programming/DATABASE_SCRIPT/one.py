import pymysql as sql

try :
    db = sql.connect(host='localhost',port=3306,user='root',password='',database='home_stuff')
    c = db.cursor()

    cmd = 'select * from daily_expenses'
    c.execute(cmd)
    data = c.fetchall()


except Exception as e : 
    print("There an error !!! ",e)
