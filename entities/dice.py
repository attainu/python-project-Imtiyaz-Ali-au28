class Dice:

    def dicePattern(dice_values):

        DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
} 
        # Holds the number of rows a given face will occupy.
        DIE_HEIGHT = len(DICE_ART[1])
        # Hold the number of columns required to draw a die face
        DIE_WIDTH = len(DICE_ART[1][0])
        # Holds a whitespace character. 
        DIE_FACE_SEPARATOR = " "

        # Will store the dice value when rolled.
        # dice_values = []
        # dice_values.append(current_chance)
        
        # Generate a list of dice faces from DICE_ART
        dice_faces = []
        for value in dice_values:
            dice_faces.append(DICE_ART[value])

        # Generate a list containing the dice faces rows
        dice_faces_rows = []
        for row_idx in range(DIE_HEIGHT):
            row_components = []
            for die in dice_faces:
                row_components.append(die[row_idx])
            row_string = DIE_FACE_SEPARATOR.join(row_components)
            dice_faces_rows.append(row_string)

        # Joining all the dice_faces_rows to print the full Dice ASCII pattern.
        dice_faces_diagram = "\n".join(dice_faces_rows)
        print(dice_faces_diagram)
            