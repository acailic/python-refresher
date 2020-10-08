friend_ages = {"Rolf":21,"Sam":22, "Anna":27}
print(friend_ages["Anna"])
friend_ages["Bob"]=33
friend_ages["Rolf"]=33

friends = [
    {"name":"Rolf","age":24},
    {"name":"Adam","age":23}
]
print(friends[0]["name"])

friend_attendence = {"Rolf":91,"Sam":92, "Anna":87}
for student in friend_attendence:
    print(f"{student}:{friend_attendence[student]}")

for student,attendance in friend_attendence.items():
    print(f"{student:{attendance}}")

if "Bob" in friend_attendence:
    print("bobo is a student")
else:
    print("hehehhe student")

attendance_values = friend_attendence.values()
print(sum(attendance_values)/len(attendance_values))

