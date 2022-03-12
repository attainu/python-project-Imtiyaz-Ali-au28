class Snake:

    def snakeCreate(text):

        try:
            global snake
            snake = {}
            tempS = int(input(text))
            if tempS <= 0:
                print("Snake should be more than ZERO")   
            for i in range(1, tempS + 1):
                temp = list(map(int, input("Enter head & tail position of the %s snake: "%(i)).split()))
                snake[temp[0]] = temp[1]     
        except ValueError:
            print("Enter number only !!\n")


    
    def isSnake(position):
        """ Checks if current position has snake head or not """
  
        if position in snake:
            return (position,snake[position])
       
