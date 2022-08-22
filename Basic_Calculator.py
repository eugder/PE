def calculator(num1, operator, num2):
    if num2 == 0 and operator == "/":
        return "Can't divide by 0!"
    return eval(str(num1) + " " + operator + " " + str(num2))


print(calculator(1, "+", 2))
