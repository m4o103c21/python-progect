#list
my_list = [5, 7, 9, 1, 1, 2]
print(my_list[0])
print(my_list[1])
index = int(input("Enter an index: "))
element = my_list[index]
print(element)

pre_last = my_list[-2]
print(pre_last)
result = my_list[0] + my_list[-1]
print(result)

#slice_list
my_list = [5, 7, 9, 1, 1, 2]
print(my_list[2:-2:2])
print(my_list[::-1])

#in_list
my_list = [5, 7, 9, 1, 1, 2]
value =int(input("Enter a number: "))
if value in my_list:
    print("This number is in list")
else:
    print("This value is not in list")


#len_list

my_list = [5, 7, 9, 1, 1, 2]
print("number of elements", len(my_list))


#string_indexing
string = "a string"
print(string[0])
print(string[2])
print(string[-1])
print(string[2:5])
print(string[:5])
print(string[2:])
print(string[2]+ string[-3:])

#in_string

string = input("Enter a string: ")
if "q" in string:
    print("There is a 'q' in the string")
else:
    print("There isn`t a 'q' in the string")


string1 = input("Enter a string: ")
print(len(string1))

    #append
my_list = []
my_list.append(3)
my_list.append(5)
my_list.append(my_list[0]+my_list[1])
print(my_list)

#del_list
my_list = [5, 1, 5, 7, 8, 1, 0, -23]
print(my_list)
del my_list[2]
print(my_list)

#mutation_list
my_list = [5, 1, 5, 7, 8, 1, 0, -23]
print(my_list)
my_list[3] = 18
print(my_list)

#traversal
my_list = [5, 1, 5, 7, 8, 1, 0, -23]
for x in my_list:
    print('{}^2 = {}'.format(x, x**2))

n = 10
fibs = [1, 1]
for i in range (n-2):
    fibs.append(fibs[i]+ fibs[i + 1])
    print(fibs)