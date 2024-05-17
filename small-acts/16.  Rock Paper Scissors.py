from random import choice

game = ["ROCK", "PAPER", "SCISSORS"]

round = eval(input("How many rounds do you want to play? "))

for i in range (round):
    computer_player = choice(game)
    player_input = input("Type your choice between ROCK, PAPER, or SCISSORS: (use only capital letters) ")
    print(f"Computer chose {computer_player}.")
    
    win = 0
    if computer_player == player_input:
        print("Draw.")
        
    elif computer_player == "ROCK" and player_input == "SCISSORS":
        print("Computer wins.")

    elif computer_player == "PAPER" and player_input == "ROCK":
        print("Computer wins.")
        
    elif computer_player == "SCISSORS" and player_input == "PAPER":
        print("Computer wins.")
        
    elif player_input == "ROCK" and computer_player == "SCISSORS":
        print("Player wins.")
        win += 1

    elif player_input == "PAPER" and computer_player == "ROCK":
        print("Player wins.")
        win += 1
        
    elif player_input == "SCISSORS" and computer_player == "PAPER":
        print("Player wins.")
        win += 1
        

print(f"\nYou won {win}/{round} matches.")

