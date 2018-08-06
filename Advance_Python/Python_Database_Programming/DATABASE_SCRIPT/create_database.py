import pymysql as sql

try : 
    db  = sql.connect(host='localhost',port=3306,user='root',password='',database='data')
    c = db.cursor()
    #name = input("Enter Database Name : ")
    #cmd = 'create database {}'.format(name)
    #c.execute(cmd)
    #c.execute('use {}'.format(name))
    #db.commit()

    table_name = input("Enter table name : ")
    n = int(input("Enter Number of columns : "))
    #d_type = [ 'int','float','timestamp','text','varchar' ]
    data = []
    for var in range(n) : 
        x = input("Enter Field Name[{}] : ".format(var+1))
        data.append(x)
    cmd = 'create table {}('.format(table_name)
    col = "{} text not null,"*n
    cmd = cmd + col.format(*data)
    cmd = cmd[:-1]+')'
    print(cmd)
    c.execute(cmd)
    print("Table Created Sucess fully")
    db.commit()
except Exception as e : 
    print("Error!!",e)



        
