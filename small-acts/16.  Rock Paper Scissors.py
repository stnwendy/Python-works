from random import choice

game = ["ROCK", "PAPER", "SCISSORS"]

rounds = int(input("How many rounds do you want to play? "))
win = 0  

for _ in range(rounds):  
    computer_player = choice(game)
    player_input = input("Type your choice between ROCK, PAPER, or SCISSORS: (use only capital letters) ")
    print(f"Computer chose {computer_player}.")
    
    if computer_player == player_input:
        print("Draw.")
        
    elif (computer_player == "ROCK" and player_input == "SCISSORS") or \
         (computer_player == "PAPER" and player_input == "ROCK") or \
         (computer_player == "SCISSORS" and player_input == "PAPER"):
        print("Computer wins.")
        
    elif (player_input == "ROCK" and computer_player == "SCISSORS") or \
         (player_input == "PAPER" and computer_player == "ROCK") or \
         (player_input == "SCISSORS" and computer_player == "PAPER"):
        print("Player wins.")
        win += 1  

print(f"\nYou won {win}/{rounds} matches.")
