n = int(input("Enter a number : "))
s = 0
num = n

while n > 0 :

    r = n % 10 
    n = n // 10 
    s = s * 10 + r

if s == num : 
    print("Palindrome")
else :
    print("Not Palindrome")
