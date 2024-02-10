# დავალება 1

def mint(list1, list2):
    return list(zip(list1, list2))

# Example usage:
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

result = mint(list1, list2)
print(result)

# დავალება 2

from functools import reduce

def product_of_elements(numbers):
    try:
        result = reduce(lambda x, y: x * y, numbers)
        return result
    except TypeError:
        print("Error: Input should be a list of numbers.")

# Example usage:
input_list = [1, 2, 3, 4, 5]

try:
    output = product_of_elements(input_list)
    print(f"The product of the elements is: {output}")
except TypeError as e:
    print(e)

# დავალება 3

input_list = [1, 2, 3, 4, 5, 6, 7]
filtered_list = list(filter(lambda x: x % 2 != 0, input_list))
print(filtered_list)

# დავალება 4

def mint(strings_list, ending):
    try:
        filtered_list = list(filter(lambda x: x.endswith(ending), strings_list))
        return filtered_list
    except TypeError as e:
        print(f"Error: {e}")

# Example usage:
input_list = ['hello', 'world', 'coding', 'nod']
ending_string = 'ing'

try:
    result = mint(input_list, ending_string)
    print(f"The filtered list is: {result}")
except TypeError as e:
    print(e)