
d = { 
        'name' : 'python',
        'version': 3.6,
        'father' : 'Guido Van Rossum',
        'named on ' : 'Monty Python',
        'method' : 'OOPS',
        'type' :'interpreted',
        'year' : 1991,
        }
print(d.items())
for key,value in d.items() : 
    print("{} = {} ".format(key,value))

