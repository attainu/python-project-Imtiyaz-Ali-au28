class Ladder:
    
    def ladderCreate(text):
        
            try:
                global ladder
                ladder = {}
                tempL = int(input(text))
                if tempL <= 0:
                    print("Ladder should be more than ZERO")
                for i in range(1, tempL + 1):
                    temp = list(map(int, input("Enter base & top position of the %s ladder: "%(i)).split()))
                    ladder[temp[0]] = temp[1]    
            except ValueError:
                print("Enter number only !!\n")


    def isLadder(position):
        """ Checks if current position has ladder base or not """

        if position in ladder:
            return (position,ladder[position])
 
