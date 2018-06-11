f  = open('housing.csv')
l = []

d = f.readline()
d = d.split(',')
l.append(d)

while True :
    d = f.readline()
    if d :
        d = d.split(',')
        d = list(map(float,d))
        l.append(d)
    else :
        f.close()
        break

"""for var in l :
    for data in var :
        print(data,end='\t')

    print() """

f = open('result.txt','w')

import json
json.dump(l,f)
f.close()



