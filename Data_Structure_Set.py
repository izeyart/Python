#Sets
my_set = {"apple", "banana", "cherry", "apple", "date"}
print(f"Initial Set: {my_set}")

#add() Operation
#Add "grape" to the set
my_set.add("grape")
print(f"After add('grape'): {my_set}")

#remove() Operation
#remove "banana" from the set
my_set.remove("banana")
print(f"After remove('banana'): {my_set}")

#Length of a Set (len())
#Get the number of items in the set
set_length = len(my_set)
print(f"Length of the set: {set_length}")

#item in xOperation(Membership Test):
#Check if cherry is in the set
is_cherry_in_set = "cherry" in my_set
print(f"Is 'cherry' in the set? {is_cherry_in_set}")

#check if "mango" is in the set
is_mango_in_set = "mango" in my_set
print(f"Is 'mango' in the set? {is_mango_in_set}")

#pop() Operation
#Remove and return an arbitrary element from the set
popped_set_item = my_set.pop()
print(f"After pop(): {my_set}, Popped Item: {popped_set_item}")

#clear() Operation
#Remove all elements from the set
my_set.clear()
print(f"Afer clear(): {my_set}")