# # operator function
def calculate (n1, n2, op):
    if op == '+':
        result = n1+n2
    elif op == '-':
        result = n1-n2
    elif op == '*':
        result = n1*n2
    elif op == '/':
        result = n1/n2
    elif op == '**':
        result = n1**n2
    else:
        raise ValueError ("Invalid operator!")
    
    return result

continue_calculating = True
while continue_calculating is True:
    num1 = float(input("Enter first number: "))
    op = input ("Enter operator (+,-,*,/,**): ")
    num2 = float(input("Enter second number: "))
    print (num1, op, num2)
    result = calculate (num1, num2, op)
    print ('=', result)
    
    go_on = input("Another calculation (y/n): ")
    if go_on == 'n':
        continue_calculating = False