#!/usr/bin/python3

if __name__ == "__main__":
    
    from calculator_1 import add, sub, mul, div 

    a = 10
    b = 5

    add_result = add(a, b)
    sub_result = sub(a, b)
    mul_result = mul(a, b)
    div_result = div(a, b)

    print("The result of adding {} and {} is {}".format(a, b, add_result))
    print("The result of subtracting {} from {} is {}".format(b, a, sub_result))
    print("The result of multiplying {} and {} is {}".format(a, b, mul_result))
    print("The result of dividing {} by {} is {}".format(a, b, div_result))
