# დავალება 1
def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    
    return fibonacci_sequence

n = int(input("Enter a number (n): "))
fibonacci_numbers = generate_fibonacci(n)
print(f"The first {n} Fibonacci numbers are: {fibonacci_numbers}")

# დავალება 2
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

string1 = str(input("Enter strin1: "))
string2 = str(input("Enter strin2: "))
result = are_anagrams(string1, string2)

if result:
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")

# დავალება 3
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number (n): "))
result = factorial(n)
print(f"The factorial of {n} is: {result}")

# დავალება 4
def count_character(input_string, target_character):
    count = 0
    
    for char in input_string:
        if char == target_character:
            count += 1
    
    return count

input_str = str(input("Enter string: "))
target_char = str(input("Enter character: "))
occurrences = count_character(input_str, target_char)
print(f"The character '{target_char}' appears {occurrences} times in the string.")