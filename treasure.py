treasure = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
'''
print('Wel Come to treasure Island:')
print('your mission is to find the treasure')
choice1 = input(f'you\'re at a crossroaddo you wnat to go? Type "Left" or "right":').lower()

if choice1 == 'left':
    choice2 = input('You\'ve come tyo a lake in the middle of the lake, Type "wait" to wait for a boat. Type "swim" to swim accross:').lower()
    if choice2 == 'wait':
        choice3 = input('You\'ve arried at the island, chose one door from "red", "blue" and "yellow"').lower()
        if choice3 == 'red':
            print('Full of fire. Game Over!')
        elif choice3 == 'yellow':
            print(f'Yeee!!! You found the treasure\n{treasure}. You Won!!!')
        elif choice3 == 'blue':
            print('You enter a room of beasts. Game Over!')
        else:
            print('Dragon attacked you. Game Over!!!')
    else:
        print('You have been attached by a angry trout. Game Over!')
else:
    print("You fell in the hole. Game Over!")