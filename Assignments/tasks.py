#დავალება 1 (ვერსია 1)
# რიცხვების მიღება
num1 = int(input("ჩაწერეთ პირველი რიცხვი: "))
num2 = int(input("ჩაწერეთ მეორე რიცხვი: "))
# ყველა ოპერაციის შესრულება
result_add = num1 + num2
result_subtract = num1 - num2
result_multiply = num1 * num2
result_divide = num1 / num2
# პასუხების გამოტანა
print(f"{num1} პლიუს {num2} უდრის {result_add}.")
print(f"{num1} მინუს {num2} უდრის {result_subtract}.")
print(f"{num1} გამრავლებული {num2}-ზე უდრის {result_multiply}.")
print(f"{num1} გაყოფილი {num2}-ზე უდრის {result_divide}.")


#დავალება 1 (ვერსია 2)
# რიცხვების მიღება
num1 = int(input("ჩაწერეთ პირველი რიცხვი: "))
num2 = int(input("ჩაწერეთ მეორე რიცხვი: "))
# ოპერაციები
operation = input("აირჩიე ოპერაცია (+, -, *, /): ")
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
else:
    result = num1 / num2
# პასუხების გამოტანა
print(f"{num1} {operation} {num2} უდრის {result}.")


#დავალება 2
# დიაგონალის სიგრძეების მიღება
diagonal1 = float(input("შეიყვანეთ პირველი დიაგონალის სიგრძე: "))
diagonal2 = float(input("შეიყვანეთ მეორე დიაგონალის სიგრძე: "))

# გამოთვლა
area = (diagonal1 * diagonal2) / 2

# შედეგის ჩვენება
print(f"რომბის ფართობი დიაგონალებით: {diagonal1} და {diagonal2} არის: {area}")


#დავალება 3
def convert_lengths(meters):
    # Conversion factors
    centimeters = meters * 100
    decimeters = meters * 10
    millimeters = meters * 1000
    miles = meters * 0.000621371  # 1 meter = 0.000621371 miles

    # Return the converted lengths
    return centimeters, decimeters, millimeters, miles

# Get user input for the length in meters
meters = float(input("Enter the length in meters: "))

# Perform the conversion
centimeters, decimeters, millimeters, miles = convert_lengths(meters)

# Display the results
print(f"{meters} meters is equal to:")
print(f"{centimeters} centimeters")
print(f"{decimeters} decimeters")
print(f"{millimeters} millimeters")
print(f"{miles} miles")


#დავალება 4
def triangle_area(base, height):
    # Formula for the area of a triangle: (base * height) / 2
    area = (base * height) / 2
    return area

# Get user input for the base and height of the triangle
base = float(input("Enter the length of the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area of the triangle
area = triangle_area(base, height)

# Display the result
print(f"The area of the triangle with base {base} and height {height} is: {area}")