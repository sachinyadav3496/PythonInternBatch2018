data = []

name = input("Enter your name : ").split('=')
data.append(name)
age = input("Enter your age : ").split('=')
data.append(age)
country = input("Enter your country : ").split('=')
data.append(country)
language = input("Enter your language : ").split('=')
data.append(language)

print(data)

print("Type conversion ")

info = dict(data)

print(info)

