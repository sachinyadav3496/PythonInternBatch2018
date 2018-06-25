f = open('my.txt')
k = open('new.txt')

n = open("merge.txt",'w')
first = f.read()
second = k.read()
print("First file data : ",first)
print("Seond file data : ",second)

print("\nBoth file are merged into merge.txt")
n.write(first)
n.write(second)
