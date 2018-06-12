def add(num):
    if num == 1 :
        return 1
    return num+add(num-1)

print(add(int(input("Enter a number : "))))

new = lambda x: 1 if x == 1 else x+new(x-1)
print(add(int(input("Enter a number : "))))


