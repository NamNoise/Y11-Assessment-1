from testhelper import test

def calculate(input1, operator, input2):
    num_1 = int(input('Enter the first number: '))
    operator_choice = input('Choose a mathematical operators (add, subtract, multiply, divide): ').lower()
    num_2 = int(input('Enter the second number: '))

    if 'add' in operator_choice:
        num_3 = num_1 + num_2
        print(num_3)
    elif 'subtract' in operator_choice:
        num_3 = num_1 - num_2
        print(num_3)
    elif 'multiply' in operator_choice:
        num_3 = num_1 * num_2
        print(num_3)
    elif 'divide' in operator_choice:
        num_3 = num_1 / num_2
        print(num_3)
    else:
        operator_choice = input('Please enter an appropriate operator: ')

print(calculate)
        
### TESTS - Run the code that calls the function to check it works.
test("Calculator 1", "20", calculate(5, "+", 15))
test("Calculator 2", "200", calculate(20, "*", 10))
test("Calculator 3", "2", calculate(100, "/", 50))
test("Calculator 4", "8", calculate(10, "-", 2))
test("Calculator 5", "10", calculate(1, "+", 9))
test("Calculator 6", "20", calculate(2, "*", 10))
test("Calculator 7", "50", calculate(100, "/", 2))
test("Calculator 8", "20", calculate(22, "-", 2))