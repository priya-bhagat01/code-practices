#Computer generates random number and player guess a number, if number matches player wins
#Player playes until he loses, how many times he wins makes a high-score
#Compares with files hi-score saved to figure out best-score

import random

def game():
    wins = 0
    loss = 0
    hiscore = 0

    while True:
        computerGuess = random.randint(1,5) #randint gives number between two numbers
        playerGuess = int(input("Enter your guess between 1 to 5: "))

        print(f"Your Guess: {playerGuess}, Computer Guess: {computerGuess}")

        if(playerGuess == computerGuess):
            wins += 1
            print("You won")
        else:
            loss += 1
            print("You lose")
            break

    with open("Problem-2.py/hi-score.txt") as f:
        hiscore = f.read()
        if hiscore:
            if(hiscore != ""):
                hiscore = int(hiscore)
            else:
                hiscore = 0

    if(str(wins) > str(hiscore)):
        with open("Problem-2.py/hi-score.txt", "w") as f:
            f.write(str(wins))

    print(f"Final score: {wins}")
    print(f"Highscore: {hiscore}")
    
    return wins

game()