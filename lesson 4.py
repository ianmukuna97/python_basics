# maths functionality
import math

x = 99

square_root = math.sqrt(x)
print("Root is ",square_root)

rounded = round(square_root, 2)
print("Rounded to two decimal places ",rounded)

#functions (args)
print(rounded)

# Call a function
y = round(8.3436363, 3)  # Corrected the syntax
print(y)

print(round(4.44444, 1))

print(math.pow(2,3))

print("----------------------")
name = 'Mzee Mzima'
print(len(name))          # Length of the string
print(name.lower())      # Convert to lowercase
print(name.upper())      # Convert to uppercase
print(name.title())      # Convert to title case
print(name.capitalize())  # Capitalize the first letter

post = "This thing is so easy and fluent"
new_post= post.replace("fluent", "flowing")
print(new_post)


