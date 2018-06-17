import random
while input("\n\n Press any key to continue : ") :
    comguess = random.randint(1,51)
    c = 1
    for c in range(1,7):
        if c == 6 :
            print("\nComputer guess was ",comguess)
            print("You such a Looser")
            break
        userguess = int(input("\n\nYour Guess:"))
        if userguess > comguess :
            print("\nThink Lower Be in Limits")
        elif userguess < comguess :
            print("\nBe Big Think Big")
        else :
            print("\nComputer guess was ",comguess)
            print("You are Winner")
            break
    
