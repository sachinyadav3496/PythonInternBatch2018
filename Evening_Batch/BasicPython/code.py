x  = 1
y = 2
while x < 10 and y < 11 :
    x += 1
    y += 1
    if x % 2 or y % 2 == 0 :
        continue
    elif x == 5 or y == 6 :
        break
    print("Hello World")
