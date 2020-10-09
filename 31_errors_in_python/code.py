def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor


# grades = [78, 99, 85, 100]
grades = []
print("Welcome to the average grade program.")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print("There are no grades yet.")
else:
    print(f"The average grade is {average}.")
finally:
    print("Thank you.")
