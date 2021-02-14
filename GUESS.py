#excersise
import random
winning_number = random.randint(1,100)
guess = 9
print("Guess the Number")
num=int(input())
game_over = False
while not game_over:
    if num == winning_number:
        guess=9-guess+1
        print(f"You Win, you guessed the number in {guess} guess")
        game_over = True
    else:
        if num > winning_number:
            print("You guessed too high")
            guess+=-1
            print(f"Number of guesses left {guess}")
            num=int(input("Guess Again: "))
        else:
            print("You guessed too low")

            guess+=-1
            print(f"Number of guessess left {guess}")
            num=int(input("Guess Again: "))
            if guess ==0:
                print("Game Over! Try next time")
                break
