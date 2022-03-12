from entities.snake import Snake
from entities.ladder import Ladder

class Player:

    def playerNumber(text):
        """ inputs the number of players by user and confirms it.
        text: str(what you want to print on the screen)
        returns: int """
    
        while True:
            try:
                temp = int(input(text))
                if temp < 5  and temp > 1:
                    return temp
                elif temp > 4:
                    print(f"{temp} Players not allowed\n")    
                elif temp <= 1:
                    print("Choose two or more Players !!\n")
            except ValueError:
                print("Enter number only !!\n")


    def checkPlayer(players,text):
        """ takes player name and checks whether it's in it
            players: dict(name -> [position])
            text: text you want to show to screen """
            
        while True:
            name = input(text).lower().strip()
            if name not in players:
                return name
            else:
                print("That player already exist please try to use abbreviation or another name..\n")            

                
    def updatePlayers(players,name,dice):
        """ updates the position of the the players
        players: dict(name -> [number])
        dice: list
        returns: dict(name -> [number]) """
        
        snakeFunc = Snake
        ladderFunc = Ladder
     
        player_p = players[name]
        if snakeFunc.isSnake(player_p + dice):
            print("A snake ∫ is found on \"%d\" and it bites you ..." %(snakeFunc.isSnake(player_p + dice)[0]))
            print("Went to %d.\n" %(snakeFunc.isSnake(player_p + dice)[1]))
            players[name] = snakeFunc.isSnake(player_p + dice)[1]
        elif ladderFunc.isLadder(player_p + dice):
            print("WooW!! a ladder is found...\nClimb it fast...")
            print("Climbed up to \"%d\".\n" %(ladderFunc.isLadder(player_p + dice)[1]))
            players[name] = ladderFunc.isLadder(player_p + dice)[1]
        elif players[name] + dice < 101:
            players[name] += dice
