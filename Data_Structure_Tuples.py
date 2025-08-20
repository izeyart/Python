my_tuple = ("red", "green", "blue", "green", "yellow")
print(f"Initial Tuple: {my_tuple}")

#Access the element at index 0
print(f"Element at index 0: {my_tuple[0]}")

#Accesss elements from index 1 to 3: (exclusive of 4)
print(f"Elements from index 1 to 3: {my_tuple[1:4]}")

#Attempt to change Tuple items

#my_tuple[0]="purple"
#print(f"ATtempted to change: {my_tuple}")
print(f"Attempting to change tuple items will result in a TypeError because tuples are immutable")

#Loop Through a Tuple
#Print each item in the tuple
print("Looping through tuple:")

for item in my_tuple:
    print("item")

#count() Operation
green_count = my_tuple.count("green")
print(f"Count of 'green': {green_count}")

#index() Operation
blue_index= my_tuple.index("blue")
print(f"Index of 'blue': {blue_index}")

#Length of a Tuple (len())
tuple_length=len(my_tuple)
print(f"Length of the tuple: {tuple_length}")