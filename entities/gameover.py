class Gameover:

    def isGameover(players):
        """ checks whether game is over or not 
        players: dict (name -> [position])
        returns: Boolean """
  
        for i in players:
            if players[i] >= 100:
                return (False,i)
        return (True,"")
        