# დავალება 1
def utf8_encode_input():
    input_string = input("Enter a string: ")
    encoded_string = input_string.encode('utf-8')
    return encoded_string

utf8_encoded = utf8_encode_input()

print(f"UTF-8 encoded string: {utf8_encoded}")

# დავალება 2
def process_string(input_string):
    stripped_string = input_string.strip()
    lowercase_string = stripped_string.lower()
    modified_string = lowercase_string + 'Python'
    final_string = modified_string.replace('python', 'Python')
    return final_string

user_input = input("Enter a string: ")

result = process_string(user_input)

print(f"Processed string: {result}")

# დავალება 3
def get_first_half(input_string):
    middle_index = len(input_string) // 2
    first_half = input_string[:middle_index]
    return first_half

user_input = input("Enter a string: ")

result = get_first_half(user_input)

print(f"First half of the string: {result}")

# დავალება 4
import string
def is_valid_string(input_string):
    if sum(c.isdigit() for c in input_string) == 1:
        valid_characters = string.ascii_letters + string.digits
        if all(c in valid_characters for c in input_string):
            return True

    return False

user_input = input("Enter a string: ")

if is_valid_string(user_input):
    print("The string is valid.")
else:
    print("The string is not valid.")

# დავალება 5
def string_to_bytes_and_back(input_string):
    byte_representation = input_string.encode('utf-8')
    print("Bytes representation:", byte_representation)
    decoded_string = byte_representation.decode('utf-8')
    print("Decoded string:", decoded_string)

user_input = input("Enter a string: ")

string_to_bytes_and_back(user_input)