import random

def instruction ():
    print("Guess the secret number between 1-10")
    return
instruction()

def trial():
    secret = random.randint(1, 10)
    attempts = 3
    while attempts > 0:
            
            try:
                guess = int(input("Guess the secret number: "))
                guessed_number = guess
                guessed_number not in range(secret)

            except ValueError:
                    print("Invalid input. Try again")
                    continue
            if guess < 1 or guess > 10: 
                print("Invalid! Your guess is out of range")
                instruction()
                continue         
            attempts -= 1
            if guess > secret:
                print(f"Failed! Too High, {guessed_number} is not the secret number. Try again.")

            elif guess < secret:
                print(f"Failed! Too low, {guessed_number} is not the secret number. Try again..")

    
            else:
                print(f"Correct! Secret number is {secret}")
                break 

            if attempts == 0:
                print(f"Max Attempts Exceeded.\nSecret number was {secret}")
                break
    return      
trial()

def replay():
    while True:
        print("Do you want to play again?\nEnter: YES/NO")
        replay_choice = input().upper()
        if replay_choice == "NO":
            print("It was a great time playing.\nCome back stronger... Bye!!!")
            exit()

        elif replay_choice == "YES":
            instruction()
            trial()

        else:
            print("You did not enter selection. Pls select an option.")
    return
replay()
