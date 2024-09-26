cars = ["bmw","maserati","audi","mercedes","ferrari"]
print(f"these are the list of cars {cars}")
print(f"the first car is {cars[0]}")
print(f"the last car is {cars[-1]}")

cars[0] = "toyota"
print(f"the first car is {cars[0]}")

print(f"the last caris {cars[-1]}")
cars[-1] = "lamborghini"
print(f"the last car is {cars[-1]}")
cars.append("bugatti")
print(cars)
cars.remove("maserati")

# looping through list
# otherwise ca;;ed iteration through the list
for car in cars:
    # print(len(car))
    # print(car)
    carRequest = input("add a new car please: ")
    cars.append(carRequest)
    print(cars)
    print(len(cars))
    print(cars)
    if len(cars) > 10:
        break

# collection = single "variable" used to storre multiple values
# list = [] ordered and changeable, Duplicates OK
# set = {} unordered and immutable, but Add/Remove OK, no duplicates 
# Tuple = () ordered and unchangeable, Duplicates OK, FASTER

fruits = ["apple", "orange", "banana", "coconut", "kiwi", "plum", "avacado"]
#print(dir(fruits)) # prints methods that come with the function
#print(help(fruits)) # tells what each method does
print(len(fruits))
print("pineapple" in fruits)

print(fruits.index("coconut"))
# fruits.append("pineapple") # adds a value to the list
# fruits.remove("apple") # removes an item from the list
# fruits.insert(0, "pineapple") # inserts an item into a specific spot in the list
# fruits.sort() # sorts the list alphabetically
# fruits.reverse() # reverses the list order
# fruits.clear()

print(fruits)

fruits[0] = "pineapple" # reassign values using that
for fruit in fruits:
    print(fruit)

# challenge
# create a list of friends
# make sure the initial list is none
friends = []
# add a new friend to the list, add at least 5 friends

# remove a friend from the list
# insert a friend at a specific index
# print the list of friends
# loop through the list and print the friends name
# see if a particular friend is in the list (boolean value)
# if list > 10 break