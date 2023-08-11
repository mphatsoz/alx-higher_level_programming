# Import functions from calculator_1.py
import calculator_1 as calc

# Define variables
a = 10
b = 5

# Call and print results
sum_result = calc.add(a, b)
sub_result = calc.subtract(a, b)
mul_result = calc.multiply(a, b)
div_result = calc.divide(a, b)

print("Sum:", sum_result)
print("Difference:", sub_result)
print("Product:", mul_result)
print("Quotient:", div_result)
