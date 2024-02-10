# დავალება 1
def main():
    my_list = []

    while True:
        command_input = input("Enter command (a - append, r - remove, e - exit): ").split()

        if not command_input:
            print("Invalid input. Please try again.")
            continue

        command = command_input[0].lower()

        if command == 'a':
            if len(command_input) != 2 or not command_input[1].isdigit():
                print("Invalid input. Please enter a valid number.")
                continue

            number = int(command_input[1])
            my_list.append(number)
            print(f"Number {number} added to the list. Current list: {my_list}")

        elif command == 'r':
            if len(command_input) != 2 or not command_input[1].isdigit():
                print("Invalid input. Please enter a valid number.")
                continue

            number = int(command_input[1])
            if number in my_list:
                my_list.remove(number)
                print(f"Number {number} removed from the list. Current list: {my_list}")
            else:
                print(f"Number {number} not found in the list. Current list: {my_list}")

        elif command == 'e':
            print("Exiting program. Final list:", my_list)
            break

        else:
            print("Invalid command. Please enter 'a', 'r', or 'e'.")

if __name__ == "__main__":
    main()


# დავალება 2

my_list = [43, '22', 12, 66, 210, ["hi"]]

# a.
index_210 = my_list.index(210)
print(f"a. Index of 210: {index_210}")

# b. 
last_element = my_list[-1]
if isinstance(last_element, list):
    last_element.append("hello")
else:
    my_list[-1] = [last_element, "hello"]

# c.
del my_list[2]
print(f"List after deleting element at index 2: {my_list}")

# d.
my_list_2 = my_list.copy()
my_list_2.clear()

print(f"my_list_2: {my_list_2}")
print(f"my_list: {my_list}")


# დავალება 3

import re

def validate_phone_number(phone_number):
    pattern = re.compile(r'^\(\d{3}\) \d{3}-\d{3}$')

    if re.match(pattern, phone_number):
        return phone_number
    else:
        return "Invalid format"

def main():
    phone_number = input("Enter a phone number in the format (123) 456-789: ")

    result = validate_phone_number(phone_number)
    print(result)

if __name__ == "__main__":
    main()