while True:
    print("BODY MASS INDEX CALCULATOR")
    userWeight=float(input("Kindly enter your weight (Kg)"))
    userHeight=float(input("Enter your height (m)"))
    BMI = (userWeight/(userHeight*userHeight))

    if BMI<18.5:
        print("Underweight")
    elif BMI<24.9:
        print("Normal weight")
    elif BMI<29.9:
        print("Overweight")
    elif BMI >29.9:
        print("Obese")

    tryAgain =input("Do you want to check again? Y/N" ).lower()
    if tryAgain!="y":
        print("Thanks for your time")
    

    

        