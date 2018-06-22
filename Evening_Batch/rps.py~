from random import choice
l = [ 'r','p','s' ]
com_Wins = [ ('r','s'), ('p','r'), ('s','p') ]
while True :
    comGuess  = choice(l)
    userGuess = input("\nYour Guess (r,p,s) : ").strip().lower()
    condition = (comGuess,userGuess)
    if condition in com_Wins :
        print("\nComputer Guess ",comGuess)
        print("Your Guess ",userGuess)
        print("You Such a Looser")
    elif comGuess == userGuess :
        print("\nComputer Guess ",comGuess)
        print("Your Guess ",userGuess)
        print("Match Tie")
        
    else :
        print("\nComputer Guess ",comGuess)
        print("Your Guess ",userGuess)
        print("You Have Won The Guess")

    ch = input("\n\n\nDo you want to play again y/n : ").strip().lower()
    if not ( ch == 'y'  or  ch == 'yes'):
        break

