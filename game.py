import random
import pyautogui as gui

def game(randomNumber: int, tries: int):
    try:
        guess = gui.prompt("Guess the number (1-500)", "Guess")
        if float(guess) > randomNumber:
            gui.alert("The number is lower", "Incorrect")
            # Increase the amount of tries
            tries += 1
            game(randomNumber, tries)
        elif float(guess) < randomNumber:
            gui.alert("The number is higher", "Incorrect")
            # Increase the amount of tries
            tries += 1
            game(randomNumber, tries)
        elif guess == str(randomNumber):
            # Tell them the amount of tries they took
            if tries == 1:
                gui.alert(f"Correct you got it first try!", "You got it!")
            else:
                gui.alert(f"Correct you got it in {tries} tries", "You got it!")
            game(random.randint(1, 500), 1)
    # If they put a non-number
    except ValueError:
        gui.alert("Not a number. Try again", "Error")
        game(randomNumber, tries)
    # If they canceled
    except TypeError:
        print("Canceled")
# Start the game
game(random.randint(1, 500), 1)
