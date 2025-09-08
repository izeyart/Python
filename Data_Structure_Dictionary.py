my_dictionary = {
    "brand": "Ford",
    "model": "Mustan",
    "year": 1964,
    "color": "red"
}
print(f"Initial Dictionary: {my_dictionary}")

#Access the value associated with the key "model"
model_Name = my_dictionary["model"]
print(f"Model: {model_Name}")

#Access the value associated with the key "year"
year_value = my_dictionary["model"]
print(f"Year: {year_value}")

#Get all keys
all_keys = my_dictionary.keys()
print(f"All keys: {list(all_keys)}")

#Get all values
all_values = my_dictionary.values()
print(f"All values: {list(all_values)}")

#Get all key-value pairs (items)
all_items = my_dictionary.items()
print(f"All items: {list(all_items)}")

#Add a new key-value pair "engine": "V8"
my_dictionary["engine"] = "V8"
print(f"After adding 'engine': {my_dictionary}")

#Change the value of "color" to "blue"
my_dictionary["color"] = "blue"
print(f"After changing 'color': {my_dictionary}")

#Remove the item with key "year" using pop()
removed_year = my_dictionary.pop("year")
print(f"After pop 'year': {my_dictionary}, Removed year:{removed_year}")


#Remove the item with the key "brand" using del
del my_dictionary["brand"]
print(f"After del my_dictionary['brand']: {my_dictionary}")


#Get the number of key-value pairs in the dictionary
dictionary_length = len(my_dictionary)
print(f"Length of the dictionary: {dictionary_length}")

#Remove all items from the dictionary
my_dictionary.clear()
print(f"After clear(): {my_dictionary}")