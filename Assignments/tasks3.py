# დავალება 1

n = int(input("Enter a number (n): "))
sum_of_numbers = 0
for i in range(1, n + 1):
    sum_of_numbers += i

print(f"The sum of numbers from 1 to {n} is: {sum_of_numbers}")


# დავალება 2

n = int(input("Enter a number: "))

while n > 0:
    print(n, end=", ")
    n -= 1
print()

# დავალება 3

import random
target_number = random.randint(1, 10)

while True:
    user_guess = int(input("Guess the number (between 1 and 10): "))
    if user_guess == target_number:
        print(f"Congratulations! You guessed the correct number: {target_number}")
        break
    elif user_guess < target_number:
        print("Try again. The correct number is higher.")
    else:
        print("Try again. The correct number is lower.")


# დავალება 4

total_sum = 0
while True:
    user_input = input("Enter a number (or 'sum' to calculate the sum): ")
    if user_input.lower() == 'sum':
        break
    try:
        number = float(user_input)
        if number > 0:
            total_sum += number
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a number or 'sum'.")
print(f"The sum of positive numbers entered is: {total_sum}")