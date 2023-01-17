# this calculator will perform simple arithmetic functions such as addition, subtraction, multiplication and division. It will also show you your most recent calculation and all of your past calculations

recent = ['lol']
history = {}

# infinite while loop which allows the user to exit the program whenever they want
while True:
    n1 = int(input('Enter first number: '))
    n2 = int(input('Enter second number: '))
    print('')

    print(f'''Enter: '+' for addition,
                   '-' for subtraction,
                   '*' for multiplication,
                   '/' for division,
                   'recent' to see last calculation,
                   'history' to see all past calculations  
                   'stop' to exit the calculator
        ''')

    op = input("Enter operation: ")


    # function to perform addition
    def add(x, y):
        sum = x + y
        print(sum)
        recent[0] = f'{x} / {y} = {sum}'
        history[f'{x} + {y}'] = sum


    # function to perform subtraction
    def sub(x, y):
        diff = x - y
        print(diff)
        recent[0] = f'{x} / {y} = {diff}'
        history[f'{x} - {y}'] = diff

        # function to perform multiplication


    def multiply(x, y):
        product = x * y
        print(product)
        recent[0] = f'{x} / {y} = {product}'
        history[f'{x} * {y}'] = product


    # function to perform division
    def div(x, y):
        quotient = x / y
        print(quotient)
        recent[0] = f'{x} / {y} = {quotient}'
        history[f'{x} / {y}'] = quotient


    if op == '+':
        add(n1, n2)

    elif op == '-':
        sub(n1, n2)

    elif op == '*':
        multiply(n1, n2)

    elif op == '/':
        div(n1, n2)

    elif op == 'recent':
        print(recent)

    elif op == 'history':
        print(history)

    elif op == 'stop':
        break

    else:
        print('Invalid input')
