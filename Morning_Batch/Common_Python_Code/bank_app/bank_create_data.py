import json
bank = {
    
    'user' : [ 'kanika','anuj','senthil','arvind' ],
    'bal' : [ 10000, 25000, 320000, 1929212],
    'acc' : [ 1001, 1002, 1003, 1004],
    'passwd' : ['abc','xyz','python','redhat'],
}

fp = open('bank.db','w')
json.dump(bank,fp)
fp.close()
