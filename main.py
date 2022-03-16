from entities.welcome import Welcome
from entities.board import Board
from entities.snake import Snake
from entities.ladder import Ladder
from entities.player import Player
from entities.dice import Dice
from entities.gameover import Gameover
import random

class Main:

    def playGame():

        # Print the welcome message at the start of the game.
        welcomeMsgFunc= Welcome
        welcomeMsgFunc.welcomeMsg()

        # Open the board images for reference
        open_boardimage = Board
        open_boardimage.displayBoard()

        # Ask user for number of snakes & their head & tail position.
        snakeFunc = Snake
        snakeFunc.snakeCreate("Enter number of snakes: ")
        
        # Ask user for number of ladder & their base & top position.
        ladderFunc = Ladder 
        ladderFunc.ladderCreate("Enter  number of ladders: ")
        
        # Ask user how many players (must be less than <=4)
        playersFunc = Player
        numbers = playersFunc.playerNumber("\nTotal number of players: ")
    
        # Take players name from user & store it in Dictionary with starting Position.
        players = {}
        ranking = ["first","second","third","fourth"]
        for i in range(numbers):
            temp_name = playersFunc.checkPlayer(players,"Enter %s player's name: " %(ranking[i]))
            players[temp_name] = 0
        
        # randomly assign the players chances
        random_chances = playersFunc.randomChance(players)
        
        # counter to keep track of the chances
        counter = 0

        # while all the player position <= 100
        gameCheckFunc = Gameover
        while gameCheckFunc.isGameover(players)[0]:
            # print whose chance is this and roll the dice
            crrnt_plyr = random_chances[counter%len(players)]
            current_pos = players[crrnt_plyr]
            if input("It's %s's chance:\nroll the DICE: " %(crrnt_plyr.capitalize())).lower().strip() == "roll".lower().strip():
                # Rolling dice randomlly from range 1 to 12.
                dice_values = []
                for i in range(2):
                    current_chance = random.randrange(1,7)
                    dice_values.append(current_chance)
                print("\nROLLING ...\n")
                print("It's a %s !.\n" %(sum(dice_values)))
                # show the dice image
                diceFunc = Dice
                diceFunc.dicePattern(dice_values) 
                final_pos = players[crrnt_plyr] + sum(dice_values) 
                print(f"\n{crrnt_plyr} rolled a {sum(dice_values)} and moved from {current_pos} to {final_pos}")
                # check for snake & ladders & update the position of player in Dictionary
                playersFunc.updatePlayers(players,crrnt_plyr,sum(dice_values))
                if not(gameCheckFunc.isGameover(players)[0]):
                    playersFunc.randomChance(players)
                print("\n")    
                print(" * "*50)
                print("\n")    
            else:
                print("Your chance is dismissed because you did'nt roll the dice !!")
            # increase the counter    
            counter += 1
        print("\n\nCongratulation, %s wins the game\n\n" %(gameCheckFunc.isGameover(players)[1]))                                                         

playFunc = Main
playFunc.playGame()
   