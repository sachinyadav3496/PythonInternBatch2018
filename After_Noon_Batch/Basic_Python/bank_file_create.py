#from json import load,dump
#load()
#dump()
import json

f = open('bank.db','w')
bank = { 
        'user' : [ 'ram', 'sam','vijay' ],
        'acc' : [ 1001, 1002, 1003 ],
        'password' : [ 'grras@123', 'something', 'redhat'],
        'balance' : [ 10000.23, 20000.45, 124322.234]
        }
json.dump(bank,f)

f.close()
print("File sucessfully created")
