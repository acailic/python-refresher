#while
#user_input = input("Would you like to play? (Y/n):")

### magic app
number = 9
while True:
    user_input = input("Would you like to play? (Y/n):")
    if user_input=="n":
        break
    user_number= int(input("Guess our number:"))
    if user_number==number:
        print("You guessed correctly")
    elif abs(number-user_number) ==1:
        print("Sorry you were off by one")
    else:
        print("Sorry no match")


friends = ["coa","sinisa","vidoje"]
# for friend in range(4)
for friend in friends:
    print(f'{friend} is my friend')

grades = [35, 89, 99, 11]
total = 0
amount= len(grades)
for grade in grades:
    total+=grade
total = sum(grades)
print(total/amount)