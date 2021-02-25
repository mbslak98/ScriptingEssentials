#Matthew Selakovich
#Mod02Tutorial

import random
import copy

def rando_insert(thing_being_inserted):
    position = random.randint(0,9)
    my_list.insert(position, thing_being_inserted)
counter = 0
my_list = []
ints_only=copy.deepcopy((my_list))

while counter < 10:
    list_item = input('Please enter a word or a number: ')
    my_list.append(list_item)
    counter += 1
else:
    print(' ')

#Task 1
    print(' ')
    print('Task 1')
    print('This list has 10 items ' + ' '+str(len(my_list) == 10))

#Task 2
    print(' ')
    print('Task 2')
    print(my_list)

#Task 3
    print(' ')
    print('Task 3')
    first_thing = my_list[0]
    my_list[0] = my_list[-1]
    my_list[-1] = first_thing
    print(my_list)
#task 4
    print(' ')
    print('Task 4')
    print(my_list[0:3], my_list[-3:])

#task 5
    print(' ')
    print('Task 5')
    for i in my_list:
        print(i)

#task 6
    print('Task 6')
    if 'cat' in my_list:
        print('There is a cat in my list')
    else:
        print('There is no cat in my list')
           
#Task 7
        print(' ')
        print('Task 7')
    another_item = input('Please insert the name of a Marvel character: ')
    rando_insert(another_item)

#Task 8
    print('\nTask 8')
    print(another_item + ' is at index ' +str(my_list.index(another_item)))

#Task 9
    
    print(' ')
    print('Task 9')
    for list_item in my_list:
        try:
            int(list_item)
            ints_only.append(int(list_item))
        except:
            continue
        
    ints_only.sort()
    print('These are the integers from the list')
    print(ints_only)

#Task 10
    print(' ')
    print('Task 10')
    my_tuple = tuple(my_list)
    print(my_tuple)

#Task 11
    print(' ')
    print('Task 11')
    try:
        my_tuple[0] = 'cat'
    except:
        print('Tuples are immutable!')

#Task 12
        print(' ')
        print('\nTask 12')
        list_in_list = [[1,2,3], ['a','b','c']]
        for i in list_in_list:
            for j in i:
                print(j)

