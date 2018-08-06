import pymysql as sql 
try : 
    db = sql.connect('localhost','root','')
    c = db.cursor()
    c.execute('create database data')
    c.execute('use data')
    db.commit()
except Exception as e : 
    print("Error!!",e)
f = open('GDP.csv')
table = f.readline().split(',')
start = table[:2]
table = start + list(map(lambda x:'year'+x,table[2:]))
table[-1] = table[-1][:-1] #removing \n from last entry
tb = table.copy()
cmd = "create table GDP(id int primary key auto_increment,{} text,{} text,"
baki = "{} float,"*(len(table)-2)
baki = baki[:-1]+')'
cmd = cmd+baki
cmd = cmd.format(*table)
c.execute(cmd)
db.commit()
mydata = []
for line in f : 
    if line : 
        data = line.split(',')
        d = list(map(lambda x:float(x) if x != '..' else 0.0,data[2:]))
        data = data[:2]+d
        mydata.append(data)
k = '{} ,'*13
k = k.format(*tb)
k = k[:-1]
cmd = "insert into gdp("+k+") values("
i = '"{}","{}",'
v = "{},"*(len(tb)-2)
v = v[:-1]
v = i+v
try : 
    for d in mydata: 
        run_cmd = cmd + v.format(*d) +')'
        print("\n\n\n{!r}".format(run_cmd))
        print("\n\n\n")
        c.execute(run_cmd)

    db.commit()
except Exception as e : 
    print("Error!",e)

