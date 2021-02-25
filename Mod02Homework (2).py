#Matthew Selakovich
#Mod02Homework

#imports
import random
import copy

card_deck = [['Ace of Spades', 'King of Spades', \
            'Queen of Spades', 'Jack of Spades', \
            '10 of Spades', '9 of Spades', \
            '8 of Spades', '7 of Spades', \
            '6 of Spades', '5 of Spades', \
            '4 of Spades', '3 of Spades', \
            '2 of Spades'], \
            ['Ace of Diamonds', 'King of Diamonds', \
            'Queen of Diamonds', 'Jack of Diamonds', \
            '10 of Diamonds', '9 of Diamonds', \
            '8 of Diamonds', '7 of Diamonds', \
            '6 of Diamonds', '5 of Diamonds', \
            '4 of Diamonds', '3 of Diamonds', \
            '2 of Diamonds'],\
            ['Ace of Clubs', 'King of Clubs', \
            'Queen of Clubs', 'Jack of Clubs', \
            '10 of Clubs', '9 of Clubs', \
            '8 of Clubs', '7 of Clubs', \
            '6 of Clubs', '5 of Clubs', \
            '4 of Clubs', '3 of Clubs', \
            '2 of Clubs'],\
            ['Ace of Hearts', 'King of Hearts', \
            'Queen of Hearts', 'Jack of Hearts', \
            '10 of Hearts', '9 of Hearts', \
            '8 of Hearts', '7 of Hearts', \
            '6 of Hearts', '5 of Hearts', \
            '4 of Hearts', '3 of Hearts', \
            '2 of Hearts']]

#List copy
game_deck =copy.deepcopy(card_deck)
no_cards=copy.deepcopy(card_deck)

#function
def draw():
    while True:
        
        if len(game_deck) <= 0 :
            print('There are no more cards ')           
        card_suit =random.randint(0,3)
        rand_card=random.randint(0,12)
        if len(game_deck[card_suit]) == 0:
            del game_deck[card_suit][rand_card]
            continue
            print(game_deck[card_suit][rand_card])
        break
    print(game_deck[card_suit][rand_card])
    return card_deck

    
#Main Body   
print('The deck has been shuffled ')
while True:
        print('How many cards would you like to draw from this deck? ')
        userinput=input()
        try:
            for i in range(int(userinput)):
                draw()
            userinput=int()
        except:
            print('That is not a number! ')
            continue
        print(' ')
        print('Press enter to draw again from this deck ')
        print('Press S to shuffle the deck and draw again ')
        print('Press Q to quit ')
        userletter=input()
        if userletter=='Q':
            print(' ')
            print('Thank you for playing. Hit enter to exit the script. ')
            input()
            exit()
        elif userletter=='S':
            print(' ')
            print('The deck has been re-shuffled ')
            copy.deepcopy(card_deck)
    
    
    
            
    
    
    


    
