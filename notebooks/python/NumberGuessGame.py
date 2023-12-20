import random

def zahlen_ratespiel():
    # Random Number between 1 and 100
    zielzahl = random.randint(1, 100)
    
    # set trys to 0
    versucheSpieler = 0

    #max trys set to 5 in this case
    versucheMax = 5

    #checkFor if any trys left
    while versucheSpieler < versucheMax:
        try:
            # Player trys to guess the number
            ratezahl = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Put in a valid number, please")
            continue
        
        # Checkfor Number Player Guessed
        if ratezahl == zielzahl:
            print("Congrats, you got the right Number")
            break
        elif ratezahl < zielzahl:
            print("The hidden number is higher")
        else:
            print("The hidden number is lower")
        
        # Add Guess to  TryCount
        versucheSpieler += 1
    
    if versucheSpieler == versucheMax:
        print(f"Sadly you didn't manage to guess the Number in {versucheMax} Trys. The Number was {zielzahl}.")
    
    # Restart Game if wanted
    neu_starten = input("Do you want to play again? (Yes/No): ")
    if neu_starten.lower() == 'yes':
        zahlen_ratespiel()
    else:
        print("Thanks for playing my little Game")

# Start Game
zahlen_ratespiel()
