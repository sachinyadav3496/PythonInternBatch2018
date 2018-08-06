import json

f = open('bank.db')
data = json.load(f)
f.close()

for key,value in data.items() :
    print("{} = {}".format(key,value))


