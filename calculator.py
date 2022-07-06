x = float(input('first number: '))
y = float(input('Second number: '))
operation = input('Operation: ')
result = None

if operation == '+':
     reslt = x + y
elif operation == '-':
     result = x - y
elif operation == '*':
     result = x*y3
elif operation == '/':
     result = x/y
else:
     print('unsupported operation')
if result is not None:
    print('result:', result)