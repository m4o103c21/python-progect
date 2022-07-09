#if
number = int(input('Enter a number:'))
if number > 5:
    print('This number is greater than five')
#if_else
x = float(input('x= '))
if x > 0:
    y = x**0.5
else:
    y = x**2
print(y)

#elif
x = float(input('x= '))
if  0 < x < 7:
    print('value is in range, let`s continue')
    y = 2*x - 5
    if y < 0:
        print('y is negative')
    elif y > 0:
        print('y is positive')
    else:
        print('y = 0')
    #elif_switch
    print("""Menu:
    1. File
    2. View
    3. Exit
    """)
    choise = input('Enter your choise: ')
    if choise =="1":
        print('You have selected "File" menu')
    elif choise == "2":
        print('You have selected "View" menu')
    elif choise =="3":
        print('Stopping')
    else:
        print('Incorrect choise')

#condition
is_ready = True
state_msg = is_ready and "Ready" or "Not ready yet"