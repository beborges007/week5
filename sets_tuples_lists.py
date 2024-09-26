# collection = single "variable" used to storre multiple values
# list = [] ordered and changeable, Duplicates OK
# set = {} unordered and immutable, but Add/Remove OK, no duplicates 
# Tuple = () ordered and unchangeable, Duplicates OK, FASTER

fruits = ["apple", "orange", "banana", "coconut", "kiwi", "plum", "avacado"]
print(dir(fruits)) # prints methods that come with the function
print(help(fruits)) # tells what each method does
print(len(fruits))
print("pineapple" in fruits)

fruits.append("pineapple") # adds a value to the list
fruits.remove("apple") # removes an item from the list
fruits.insert(0, "pineapple") # inserts an item into a specific spot in the list
fruits.sort() # sorts the list alphabetically
fruits.reverse() # reverses the list order
fruits.clear()

print(fruits)

fruits[0] = "pineapple" # reassign values using that
for fruit in fruits:
    print(fruit)