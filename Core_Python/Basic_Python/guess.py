from random import randint
while True :
    comGuess = randint(1,50)
    x = 1
    while x <= 5 :
        userGuess = int(input("\nYour Guess (1,50) : "))
        if comGuess > userGuess :
            print("\nBe Big Think Big")
        elif comGuess < userGuess :
            print("\nBe in Limits Think Lower")
        else :
            print("\nComputer Guess was ",comGuess)
            print("\nYou Have Won This Game")
            break
        if x == 5 :
            print("\nComputer Guess was ",comGuess)
            print("\nYou Such a Looser")
        x  = x + 1
    ch = input("\n\nDo want to play again y/n : ").strip().lower()
    if ch == 'y' or ch == 'yes' :
        pass
    else :
        break
