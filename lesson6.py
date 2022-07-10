number = int(input('Enter a number:  '))

print('Binary:    ', bin(number))
print('Octal:   ', oct(number))
print('Hexadecimal:   ', hex(number))

#reversed_example
for i in range(5):
    print(i)

print()
print()

for i in reversed("asdf"):
    print(i)

#min_max
a = float(input('A = '))
b = float(input('B= '))
c = float(input('C = '))
print("min:", min(a, b, c))
print("max: ", max(a, b, c))



#scoping_example
def function():
    print(var)
var = 'global variable'
function()


def function():
    global var
    var = 'new variable'
    print(var)
var = "global variable"
function()
print(var)


#factorial

def nonrecursive_factorial(n):
    result = 1
    for multiplier in range(2, n + 1):
        result *= multiplier
    return result


print(nonrecursive_factorial(5))

def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)

print(recursive_factorial(6))

#hanoy
def hanoi(n, a, b, c):
    if n != 0:
        hanoi(n-1, a, c, b)
        print('transfer a ring from', a, 'to', c)
        hanoi(n-1, b, a, c)


hanoi(8, 'A', 'B', 'C')
