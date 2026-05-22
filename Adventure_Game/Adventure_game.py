name=input("please enter your name , adventurer ")

print(f"Welcome to the jungle, {name}! ")

answer=input('You are on a dirt road, it has to come to an end and you can go left or right. Which way would you like to go? ').lower()

if answer== 'left':
    answer=input('You come into a river, you can walk around it or swim across it. Type walk to walk around or swim to swim across')
    if answer=='walk':
        print('You walked for many miles, ran out of water and you lost the game!')
    elif answer=='swim':
        print('you swam across and were eaten by an alligator. Game over!')
    else:        
        print('Not a valid option. You lose!')
elif answer=='right':
    answer=input('You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ')
    if answer=='cross':
        print('you crossed the bridge and found a stranger .Do you talk to them or ignore them (talk/ignore)? ')
        if answer=='talk':
            print('you talked to the stranger and they gave you gold. You win!')
        elif answer=='ignore':
            print('you ignored the stranger and they were offended and you lose!')
    elif answer=='back':
        print('you go back and a tiger eats you. Game over!')

else:
    print('Not a valid option. You lose!')