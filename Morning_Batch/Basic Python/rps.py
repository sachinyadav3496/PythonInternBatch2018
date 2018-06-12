p1 = [ ('r','s'),('p','r'),('s','p')]
from random import choice
while True :
    ch1 = choice(['r','p','s'])
    ch2 = input("Player2: ")
    if ch1 == ch2 : 
        print("Match Tie")
    elif (ch1,ch2) in p1 :
        print("Computer Choice was : ",ch1)
        print("Player Choice was : ",ch2)
        print("Player1 is the Winner")
    else :
        print("Computer Choice was : ",ch1)
        print("Player Choice was : ",ch2)
        print("Player2 is the Winner")
    
    ch = input("Do want to continue (y/n) : ").strip().lower()
    if ch == 'y' or ch == 'yes' :
        continue
    else :
        break
