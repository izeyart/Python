userInput=input("Enter anything: ")
cleanChar=userInput.strip()
countChar=0
for char in cleanChar:
    countChar+=1

print(f'{countChar} characters')


countWord=0
cleanWord=userInput.split()
for word in cleanWord:
    countWord+=1
print(f'{countWord} words')


cleanSen=userInput.split(".")
print(f'{len(cleanSen)} sentence(s)')
    