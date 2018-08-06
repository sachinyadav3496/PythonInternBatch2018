s = int(input("Starting Point : "))
e = int(input("Ending Point : "))

for var in range(s,e+1):
    s = "{:>15}{:>15}{:>15}{:>15}".format(var,var**2,var**3,var**4)
    print(s)
