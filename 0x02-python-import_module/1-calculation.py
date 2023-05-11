#!/usr/bin/python3
import calculator_1 as calc

a = 10
b = 5

add_result = calc.add(a, b)
sub_result = calc.sub(a, b)
mul_result = calc.mul(a, b)
div_result = calc.div(a, b)

print("The result of adding {} and {} is {}".format(a, b, add_result))
print("The result of subtracting {} from {} is {}".format(b, a, sub_result))
print("The result of multiplying {} and {} is {}".format(a, b, mul_result))
print("The result of dividing {} by {} is {}".format(a, b, div_result))
