import pymysql as sql
try :
    db = sql.connect(host='localhost',port=3306,user='root',password='',database='bankapp')
    c = db.cursor()
except Exception as error :
    print("There is an error in Data Base connectivity")
    print("Please That your data base server is running and active")
    print("Error!!",error)

def entry():
    name = input("User Name : ")
    password = input("Password : ")
    bal = float(input("Balance : "))
    cmd = 'insert into data(name,bal,password) values("{}",{},"{}")'.format(name,bal,password)
    c.execute(cmd)
    db.commit()
    print("user sucess fully created")

def fulldata():
    cmd = 'select * from data'
    c.execute(cmd)
    data = c.fetchall()
    for var in data :
        print(*var)
def fetch():
    acc = int(input("Acc no"))
    import getpass
    pas = getpass.getpass()
    cmd = 'select * from data where acc_no = {} '.format(acc)
    s = c.execute(cmd)
    if s == 0 :
        print("No such Account Exist")
    else :
        data = c.fetchone()
        if pas == data[3] :
            "Sucess Fully Login"
            print(*data)
        else :
            print("Incorrect Password ")
if __name__ == "__main__" :

    entry()
    fulldata()
    fetch()
