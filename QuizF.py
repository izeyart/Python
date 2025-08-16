secretAnswer="phobia"
guessedAnswer=""
guesses=3
score=0
while guessedAnswer!=secretAnswer and guesses>0:
    guessedAnswer=input("What is the by name of Hearts of oak")
    guesses-=1
    if guessedAnswer==secretAnswer:
        score+=1
        print("Correct")
        print("Your score is "+str(score))
    elif guessedAnswer!=secretAnswer and guesses==0:
        score+=0
        print("Wrong")
        print("Your score is "+str(score))
    else:
        print("Wrong, Try Again")
hsecretAnswer="fabulous"
hguessedAnswer=""
hguesses=3
score=0
while hguessedAnswer!=hsecretAnswer and hguesses>0:
    hguessedAnswer=input("What is the by name of Asante Kotoko F.C?: ")
    hguesses-=1
    if hguessedAnswer==hsecretAnswer:
        score+=1
        print("Correct")
        print("Your score is "+str(score))
    elif hguessedAnswer!=hsecretAnswer and hguesses==0:
        score+=0
        print("Wrong")
        print("Your score is "+str(score))
    else:
        print("Wrong, Try Again")