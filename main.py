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
        diceFunc = Dice
        random_chances = diceFunc.randomChance(players)
        
        # counter to keep track of the chances
        counter = 0

        # while all the player position <= 100
        gameCheckFunc = Gameover
        while gameCheckFunc.isGameover(players)[0]:
            # print whose chance is this and roll the dice
            crrnt_plyr = random_chances[counter%len(players)]
            current_pos = players[crrnt_plyr]
            if input("It's %s's chance:\nroll the DICE: " %(crrnt_plyr.capitalize())).lower().strip() == "roll".lower().strip():
                # Rolling dice randomlly from range 1 to 6.
                current_chance = random.randrange(1,7)
                print("\nROLLING ...\n")
                print("It's a %s !." %(current_chance))
                # show the dice image
                diceFunc.dicePattern(current_chance) 
                final_pos = players[crrnt_plyr] + current_chance 
                print(f"\n{crrnt_plyr} rolled a {current_chance} and moved from {current_pos} to {final_pos}")
                # check for snake & ladders & update the position of player in Dictionary
                playersFunc.updatePlayers(players,crrnt_plyr,current_chance)
                if not(gameCheckFunc.isGameover(players)[0]):
                    diceFunc.randomChance(players)
            else:
                print("Your chance is dismissed because you did'nt roll the dice !!")
            # increase the counter    
            counter += 1
        print("\n\nCongratulation, %s wins the game\n\n" %(gameCheckFunc.isGameover(players)[1]))                                                         

playFunc = Main
playFunc.playGame()
   