correctPassword="secret"
userAttempt=""
attemptLeft=3
while userAttempt!=correctPassword and attemptLeft>0:
    userAttempt=input("Enter password (attempts left: "+str(attemptLeft)+"):")
    attemptLeft-=1
    if userAttempt==correctPassword:
        print("Access Granted")
    else:
        print("Acces Denied!")