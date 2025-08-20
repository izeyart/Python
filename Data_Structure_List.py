my_List=["apple", "banana", "cherry", "date", "banana"]
print(f"Initial List: {my_List}")

#del() Operation
del my_List[2]
print(f"After del my_List[2]: {my_List}")

#append() Operation
my_List.append("grape")
print(f"After append ('grape'): {my_List}")

#extend() Operation
my_List.extend(["kiwi","lemon"])
print(f"After extend(['kiwi', 'lemon']): {my_List}")

#insert() Operation
my_List.insert(1,"orange")
print(f"After my_List.insert(1,'orange'): {my_List}")

#pop() Operation
popped_item=my_List.pop()
print(f"After pop(): {my_List}, Popped Item: {popped_item}")

#remove() Operation
my_List.remove("banana")
print(f"After remove('banana'): {my_List}")

#reverse() Operation
my_List.reverse()
print(f"After reverse (): {my_List}")

#sort() Operation
my_List.sort()
print(f"After sort(): {my_List}")