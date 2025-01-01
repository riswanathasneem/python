num1=float(input("enter a number:"))
num2=float(input("enter 2nd number:"))
addition =num1+num2
print("the result of adding", num1,"and",num2,"is",addition)
subtraction= num1-num2
print("the result of subtracting",num1,"and",num2,"is",subtraction)
product=num1*num2
print("the result of multiplying",num1,"and",num2,"is",product)
if num2!=0:
    division=num1/num2
    print("the result of dividing",num1,"and",num2,"is",division)
else:
    print("division by zero is undefined.")
if num2!=0:
    modulus=num1%num2
    print("the result of modulus operation with",num1,"and",num2,"is",modulus)
else:
    print("modulus by zero is undefined")
if num2!=0:
    floor_division=+num1//num2
    print("the result of division operation with",num1,"and",num2,"is",floor_division)
else:
    print("floor division by zero is undefined.")