import random 

Top_of_range = input("Enter a number : ")

if Top_of_range.isdigit():
    Top_of_range = int(Top_of_range)
    if Top_of_range <= 0 : 
        print("Please enter a number greater than 0 next time.")
        quit()
else:
    print("Please enter a number next time.")
    quit()

random_number = random.randint(0,Top_of_range)

guesses=0
while True:
    guesses += 1
    guess = input("Make a guess : ")
    if guess.isdigit():
        guess=int(guess)
    else:
        print("Please enter a number next time.")
        continue
    if guess == random_number:
        print("You got it right!")
        break
    else:
        if guess > random_number:
            print("You were above the number!")
        else:            
            print("You were below the number!")
    
print(f"You got it in {guesses} guesses!")