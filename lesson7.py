#while_example1

responce = ""
while responce != "exit":
    responce = input("Type 'exit' to exit: ")

#while_example2
n = 1
while n <=3:
     print('n = ', n)
     n += 1

#while_example3
number = 0
while number <= 0:
    number = int(input('Enter a positive integer: '))

print("You have entered", number)

#break_example

while True:
    print('Enter "exit" to exit loop')
    response = input(">")
    if response == "exit":
        break
print("loop has stopped")


#break_example2
while True:
    print("Menu: ")
    print("1. Enter your name")
    print("2. Print greeting")
    print("3. Quit")

    response = input("Please choose an action: ")

    print()
    if response =="1":
        name = input("Enter your name:")
    elif response =="2":
        if name:
            print("Hello, ", name, "!", sep = "")
        else:
            print("I don`t know your name.")
    elif response == "3":
        break
    else:
        print("Incorrected input")
        print()

#continue_example

number = 0
while number < 10:
    number += 1
    if number == 5:
        continue
    print("current number is", number)

#while_else_example
attempts_left = 3
while attempts_left > 0:
    attempts_left -=1
    password = input("Enter your password"
                     "(you have {} attempts left):".format(attempts_left + 1))
    if password == "98eaxc":
        print("Access granted")
        break
else:
    print("Access denied")


#for_example
for i in range(10):
    print("i = ", i)

#neste_loops
for  row in range(5):
    for column in range(30):
        print("*", end = "")
    print()