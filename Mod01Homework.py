#Matthew Selakovich
#Mod01Homework
import random
print('Welcome to the vending machine, you can enter values of 5, 10, or 25 in payment.')
print('What type of soda would you like')
sodachoice= input()
SODA = 100
for i in range (0,7):
    random_value = random.randint(-3,3)
    pricevariance= random_value * 5
    
#defining the amount remaining
coinsleft = SODA + pricevariance
print('The current price of '+sodachoice + ' is ' + str(coinsleft)+' cents')
#main loop
while True:
    #requirement met
    if coinsleft == 0:
        print('Enjoy your '+ sodachoice)
        print()
        print()
        input()
        break
    #balance remaining over 0
    elif coinsleft>0:
        coins =int(input('Enter a coin amount: '))
        if coins == 5:
            coinsleft = coinsleft - 5
            if coinsleft>0:
                print('you still owe '+ str(coinsleft))
            else:
                continue
        elif coins == 10:
            coinsleft = coinsleft - 10
            if coinsleft>0:
                print('you still owe '+ str(coinsleft))
            else:
                continue
        elif coins == 25 :
            coinsleft = coinsleft - 25
            if coinsleft>0:
                print('you still owe '+ str(coinsleft))
            else:
                continue
        else:
            print('that is not a valid amount')
            continue
        #Refund amount 
    elif coinsleft<0:
        print('you have been refunded '+str(abs(coinsleft))+' cents.')
        print('Enjoy your '+ sodachoice)
        print()
        print()
        input()
        break
    else:
        break
