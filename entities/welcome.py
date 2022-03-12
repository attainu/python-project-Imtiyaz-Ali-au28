from time import sleep
from tkinter import CENTER
from pyfiglet import figlet_format


class Welcome:

    def welcomeMsg():
        print("\n"+figlet_format(" WELCOME TO SNAKE-LADDER", font = "standard",width = 150, justify=CENTER),"\n")
        sleep(0.3)
        print(r"""        /\		     |-----|
       //\\                  |-----|
       ||                    |-----|
       || SNAKES     and     |-----| LADDERS
       ||                    |-----|
    \\//                     |-----|
     \/	                     |-----|
    """)
        sleep(0.3)
        print('''Version: Latest Version\nDeveloped by: Ali@imtiyaz''')
        print("\n"+" HOW TO PLAY THE GAME ".center(100,"-"),"")
        sleep(0.3)
        msg = """
        1. The players will move their pieces from left to right, starting at 1, 
        following the numbers on the board, then the next row from right to left and repeat. 
            Take it in turns to roll the dice. 
            Move forward the number of spaces shown on the dice.
        2. When a player lands on a top of a snake, their playing piece will slide down to the bottom of the snake.
        3. When a player lands at the base of a ladder, it immediately climbs to the top of the ladder.
        4. The first player that reaches the highest space on the board, 100, wins the game.
        5. Hit enter to roll the dice.

        """
        print(msg)

