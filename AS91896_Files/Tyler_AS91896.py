print("Welcome to my baseball game.")

import random

def pitch():
    return random.choice(["strike", "ball", "hit", "home_run", "out"])


def play_game():
    play_score = 0
    strikes = 0
    balls = 0
    out = 0
    
    while out < 3:
        input("Press enter to swing.")
        result = pitch()
        if result == "strike":
            strikes += 1
        if result == "ball":
            balls += 1
        if result == "hit":
            print("Hit! Runner on base.")
            return "hit"
        if result == "out":
            print("Out!")
            return "out"
        if result == "home_run":
            print("Home run!")
            play_score += 1
            return "FINISH"
        if strikes == 3:
            print("Strikeout!")
            return "out"
        if balls == 4:
            print("Walk!")
            return "walk"

replay = "YES"
while replay == "YES":
    play_game()
       
