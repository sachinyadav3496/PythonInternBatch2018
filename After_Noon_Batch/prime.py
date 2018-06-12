s = int(input("Enter start Point : "))
e = int(input("Enter ending Point : "))
import math
total_prime = 0
while s <= e :
    num = s
    if num <= 1 :
        print("Error!! Invalid range")
        exit(0)
    elif num == 2 :
        print(num,end='\t')
        total_prime += 1
        
    check = 2
    sq = math.sqrt(num)
    sq = int(sq) + 1

    while check <= sq :
    
        k = num % check 
        if k == 0 :
            break
        elif check == sq :
            print(num,end='\t')
            total_prime += 1
        check = check + 1
    s = s + 1
print("Total Prime number in this range are : ",total_prime)
