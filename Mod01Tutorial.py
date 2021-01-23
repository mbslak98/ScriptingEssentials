#Matthew Selakovich
#Tutorial 1
import sys

print('Task 1')

print ('Hello World')
input()

print('Task 2')

user_new = input('Please enter an integer: ')
print (user_new)
input()

print('Task 3')

##print(user_new * 3)
##int(user_new)

user_new = int(user_new)
#converted_user_new = int(user_new) pay attention to data types
converted_user_new = int(user_new)
print(user_new*3)
print(converted_user_new*3)
user_new =str(user_new)
converted_user_new=str(converted_user_new)
print(user_new*3)
print('I entered ' + user_new)

print('')
print('Task 4')

##(count by, count to, end at)

for i in range (1,21,1) :
   if (i % 2) == 0:
       print('Even')
   elif i == 7:
           print('7')
   else:
        print('Odd')
print('')    
print('Task 5')

for l in range (1,int(input('Enter a number over with a greater value than 13: '))+1,1) :
   if (l % 2) == 0:
       print('Even')
   elif l == 7:
           print('Lucky')
   elif l == 13:
      print('Unlucky')
   else:
        print('Odd')
print('')
print('Task 6')


while True:
        username = input('Enter your Last name: ')
        if username == 'Selakovich':
            break
        else:
            continue
print('')
print('Task 7')

counter= 0
while counter < 10:
    print(counter)
    counter += 1
print('')
print('Task 8')

import random

for i in range (0,5):
    random_value = random.randint(-10,10)
    print (random_value,end=" ")
print()
print()
print('Enter will end the script')
input()
   
