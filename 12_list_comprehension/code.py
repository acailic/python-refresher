numbers = [1,3,5]
doubled =[num*2 for num in numbers]
for num in numbers:
    doubled.append(num*2)

friends = ["Rolf","Sam", "john"]
starts_s= [friend for friend in friends if friend.startswith("S")]
# it creates a new list
#starts_s=friends
'''
for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)
'''
print(starts_s)
print(friends is starts_s)
print("friends: ", id(friends),"start_s:",id(starts_s))

