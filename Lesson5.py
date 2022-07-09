#function_example
def print_numbers(limit):
    for i in range(limit):
        print(i)

n = int(input('n = '))
print_numbers(n)

#example
def hello():
    print('hello, world!')
    print('This text gets printed from a function')

hello()
hello()

def print_numbers(limit):
    for i in range(limit):
        print(i)
def main():
    print_numbers(3)
    print()
    print_numbers(8)
    print()
main()

def add_numbers(first, second):
    print('add_numbers called with', first, second)
    return first + second
add_numbers(9, 10)
result = add_numbers(2,3) - add_numbers(1,2)
print(result)

def function(x):
    if x < 0:
        return x*2
    else:
        return x*3

def main():
    for i in range(-3, 4):
        y = function(i)
        print('function (', i, ') = ' , y, sep = '')
main()
print()
print()
print()
#example5

def print_info(object_name, color, price):
    print('Object: ', object_name)
    print('Color: ', color)
    print('Price: ', price)
    print()
print_info('pen', 'blue', 18)
print_info(object_name='pen',
           color='blue',
           price = 1)
print_info(price=5, object_name='cup', color='orange')