from PIL import Image

class Board:
        
    def displayBoard():
        """ Opens the board image of Snake-ladder
        for reference to enter snake & ladder position
         """

        ImagePath = "assets/images/board_image.png"
        img = Image.open(ImagePath)
        img.show()
