friends = {"Bob","Anne","Rolf"}
abroad = {"Bob","Anne"}
local_friends = friends.difference(abroad)
print(local_friends)

friends_total = friends.union(abroad)
print(friends_total)
friends_both = abroad.intersection(friends)
print(friends_both)