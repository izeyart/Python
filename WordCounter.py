userInput=input("Enter anything: ")
countChar=0
for char in userInput:
    countChar+=1

print(f'{countChar} characters')


countWord=0
breakWord=userInput.split()
for word in breakWord:
    countWord+=1
print(f'{countWord} words')

num_Of_Sen=userInput.split(".") + userInput.split("?") + userInput.split("!")
print(f'{len(num_Of_Sen)-3} sentence(s)')
