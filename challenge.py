# challenge
# create a list of friends
# make sure the initial list is none
friends = []
# add a new friend to the list, add at least 5 friends
friends = ["AJ","Linda","Leeroy","Harry"]
print(friends)
for friend in friends:
    friendRequest = input("Who would you like to friend: ")
    friends.insert(2,friendRequest)
    print(friends)
    # if friends > 5:
    #     removeFriend = input("Who do you want to remove from the list")
    #     friends.remove(removeFriend)
    #     print(friends)
# remove a friend from the list
# insert a friend at a specific index
# print the list of friends
# loop through the list and print the friends name
# see if a particular friend is in the list (boolean value)
# if list > 10 break