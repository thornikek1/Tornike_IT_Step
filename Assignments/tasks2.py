# დავალება 1
num_list = [44, 23, 11, 8, 20, 56, 33, 55]

# Get user input for the number to check
user_input = int(input("Enter a number: "))

# Check if the entered number is in the list
if user_input in num_list:
    print(f"The number {user_input} is in the list")
else:
    print(f"The number {user_input} is not in the list")


# დავალება 2

user_input2 = int(input("Enter an integer: "))

if user_input2 % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


# დავალება 3 

st1 = "Hello"
st2 = "Hello"

if st1 is st2:
    print("Same object")
else:
    print("Different object")


#დავალება 4 

num_list2 = [44, 23, 11, 8, 20, 56, 33, 55]
user_input3 = int(input("Enter a number: "))

# Check the conditions
if user_input3 > num_list2[2] and user_input3 < num_list2[-1]:
    print ("More than list elements")
elif user_input3 == num_list2[5]:
    print ("Equal")
else:
    print ("None of the conditions were met")