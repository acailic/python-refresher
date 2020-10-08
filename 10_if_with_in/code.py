friends = {"Rolf","Bob","Jen"}
movies_watched = {"Matrix","Her","Superman"}

user_movie = input("Enter movie that you watched:")


if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("i havent watched that yet")


### magic app
number = 9
user_input = input("Do you want to play a game: ").lower()
## can use in ("y","Y")
## number-user_number in (-1,1):
if user_input=='y':
    user_number= int(input("Guess our number:"))
    if user_number==number:
        print("You guessed correctly")
    elif abs(number-user_number) ==1:
        print("Sorry you were off by one")
    else:
        print("Sorry no match")
