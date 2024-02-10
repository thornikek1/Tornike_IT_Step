# დავალება 1

int_list = [10, 20, 30, 40]

def add_to_int_list(number):
    global int_list
    int_list.append(number)

number_to_add = int(input("Enter a number (n): "))
add_to_int_list(number_to_add)

print(f"Updated int_list: {int_list}")

# დავალება 2

def calculate_sum(numbers):
    return sum(numbers)

number_list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
total_sum = calculate_sum(number_list)

print(f"The sum of the numbers is: {total_sum}")

# დავალება 3

gl_str = "Global"

def create_local_variable():
    gl_str = "Local"
    return gl_str

local_variable_value = create_local_variable()
print(f"The value of the local variable is: {local_variable_value}")
print(f"The value of the global variable is still: {gl_str}")

# დავალება 4

def sum_of_digits(number):
    if number == 0:
        return 0
    else:
        return number % 10 + sum_of_digits(number // 10)

input_number = int(input("Enter a number (n): "))
result = sum_of_digits(input_number)
print(f"The sum of the digits of {input_number} is: {result}")

# დავალება 5

def reverse_string(input_str):
    if len(input_str) == 0:
        return input_str
    else:
        return input_str[-1] + reverse_string(input_str[:-1])

input_string = str(input("Enter string: "))
result = reverse_string(input_string)
print(f"The reverse of '{input_string}' is: {result}")