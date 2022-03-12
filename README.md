# Snake & Ladder



## Requirements


Python version 3.0 or above. Visit the link https://www.python.org/downloads/ to download and install Python

required Any IDE for run the application. like "VScode"



## Usage


    - Download ZIP or Clone the Repository using given code below:

        >> git clone https://github.com/attainu/python-project-Imtiyaz-Ali-au28.git
    
    - Find main.py in snake-ladder/main.py and Run it.
    
    - Give Appropriate Inputs.
    
    - Enjoy the Game.



## Introduction


Snakes and ladders is an ancient Indian board game that’s regarded today as a worldwide classic. It requires two or more 

players and takes place on a board with numbered, gridded squares. Throughout the board, there are snakes and ladders 

which connect different squares. Players roll a die and navigate the board. Landing on a ladder advances a player to a 

square further up the board, while landing on a snake means they have to go back to a

previous square.

The aim of the game is to reach the final square. The game is a race that’s based on sheer luck, and is popular with 

children.



## Features


- Eye-Catching ASCII patterns

- Command-line(CLI) based game

- Straightforward user interface

- Easier gameplay

- Multiplayer gaming

- Platform independent

- Input/Output(I/O) routines



## Documentation


This project is aimed at developing a multiplayer Snake and Ladder game, whick can be played on command line interface. 

This game has been built using Python.




### Libraries Used:



    1. tkinter =  I have used this library to use one of its method called "CENTER" which configure and align the text  
       
       at the center.

    2. Python Imaging Library(PIL): It is a free and open-source additional library for the Python programming language 
       
       that adds support for opening, manipulating, and saving many different image file formats.

    3. Pyfiglet: This library takes ASCII text and renders it in ASCII art fonts. figlet_format method convert ASCII 
       
       text into ASCII art fonts.

    4. Random : This library helps to choose an element randomly among a given list or to get a random number or shuffle 
       
       elements randomly. I used this library to choose a random number from 1 to 6, as in a dice.

    5. Time : This library provides various time-related functions. I used the sleep method of this library to make the 
       
       user experience of this game better.




### Modules:



    1. welcome: This module is to print welcome message when user starts the game.
       This module has a class Welcome with a method:
            - welcomeMsg()

    2. board: This module is not the major part of this application. I have added for reference
       only. It open the picture of the snake-ladder game.
       This module has a class Board with a method:
            - displayBoard()

    3. dice: This module is very exiting beacause it prints the ASCII pattern of a dice & 
       creates random chances of the players.
       This module has class Dice with two methods:
            - randomChance(players)
            - dicePattern(current_chance)

    4. player: This module to take input of number of players
       from users, creating players and storing their name
       and initial position in the dictionary as key:value pairs and updating 
       the players dictionary as position change.
       This module has a class Player with three methods:
            - playerNumber(text)
            - checkPlayer(players,text)
            - updatePlayers(players,name,dice)

    5. snake: This module is to take input from user for number of snakes 
       the user wants in the gameand check if current position has snake head or not.
       It has a class Snake with two method:
            - snakeCreate(text)
            - isSnake(position)

    6. ladder: This module is to take input from user for number of ladder
       the user wants in the game and check if current position has ladder base or not..
       It has a class Ladder with two methods:
            - ladderCreate(text)
            - isLadder(position)

    7. gameover: This module is to checks whether game is over or not & returns boolean value
       It has a class Gameover with a method:   
            - isGameover(players)  

    8. main: This module is the centeral processing unit of this appication which manages to 
       connect & run the whole application.
       It has a class Main with a method:
            - playGame()           




### Methods/Functions:



    1. welcomeMsg(): This function is very basic whose operation is to print the Welcome message.

    2. displayBoard(): This function operation is to open the Board image.

    3. randomChance(players): This function operation is to create random chances for players. It 
       takes a players dictionary as a parameter, copies in the list, shuffle them & return.

    4. dicePattern(current_chance): This functions operation exciting beacause it's operations is to 
       print dice ASCII pattern. it takes one parameter which is curent_chance meaning the current random
       dice value.

    5. playerNumber(text): This function operations is to take number of players as input from the user. 
       it also limits user to minimum(2) & maximum(4) numbers of players. I have used try-except block 
       in this function. It takes one parameter text which is text shown to the user when taking input.

    6. checkPlayer(players,text): This function operation is to take the player names or abbreviation from 
        the user & stores or checks the player name from the player dictionary so that every player name is 
        unique in the game. It takes two parameter player which is dictionary & text which is text shown to 
        the user when taking input.  

    7. updatePlayers(players,name,dice): This function operation is to check whether the final_position with
       regards to this code has snake head, ladder base or none of two & updates the position in the player
       dictionary. This function takes three parameters players dictionary, current player name or abbreviation
       who chance is and current dice value.

    8. snakeCreate(text): This function operations is to ask user for the number of snakes he/she wants in the 
       game & stores in the snake dictionary. I have used try-except block in this function. This functions takes
       one parameter text which is text shown to the user when taking input.

    9. isSnake(position): This function operation is to check with snakes dictionary if current position has snake 
       head or not. It takes one parameter position which is the final_position with regards to this code.

    10. ladderCreate(text): This function operations is to ask user for the number of ladder he/she wants in the 
       game & stores in the ladder dictionary. I have used try-except block in this function. This functions takes
       one parameter text which is text shown to the user when taking input.

    11. isLadder(position): This function operation is to check with ladder dictionary if current position has ladder 
       base or not. It takes one parameter position which is the final_position with regards to this code.
  
    12. isGameover(players): This function operations is to cheack whether game is over or not by checking if any one 
        players have reached 100th position or not then return bollean value which will run or stop the loop in the 
        main.py file.  
