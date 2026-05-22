import random
print("Welcome to Rock, Paper, Scissors!")
user_wins=0
computer_wins=0
options=['rock','paper','scissors']
while True:
    user_pick = input("Enter either rock,paper,scissors , or q to quit: ").lower()
    if user_pick == 'q':
        break
    
    if user_pick not in options :
        continue

    random_number=random.randint(0,2)
    #rock:0 , paper:1 , scissors:2
    computer_pick=options[random_number]

    print(f"computer picked {computer_pick} .")
    if user_pick =='rock' and computer_pick=='scissors':
        print("you won!")
        user_wins+=1
    elif user_pick =='paper' and computer_pick=='rock':
        print("you won!")
        user_wins+=1
    elif user_pick =='scissors' and computer_pick=='paper':
        print("you won!")
        user_wins+=1    
    elif user_pick =='rock' and computer_pick=='rock':
        print("it's a tie! ")
    elif user_pick =='Paper' and computer_pick=='Paper':
        print("it's a tie! ")
    elif user_pick =='Scissor' and computer_pick=='Scissor':
        print("it's a tie! ")
    else : 
        print('Computer won!')
        computer_wins+=1

print("you won ",user_wins)
print(f"computer won ,{computer_wins}")

print("Good Bye!")
    
        

