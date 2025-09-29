import math

num = float(input("Enter a number: "))

square_root = math.sqrt(num)
natural_log = math.log(num) if num > 0 else "Undefined (logarithm of non-positive number)"
sine_value = math.sin(num)

print(f"\n--- Results ---")
print(f"Square root of {num} = {square_root}")
print(f"Natural logarithm of {num} = {natural_log}")
print(f"Sine of {num} (radians) = {sine_value}")
