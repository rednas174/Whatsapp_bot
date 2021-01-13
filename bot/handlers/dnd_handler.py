import random
import math

from numpy.random import randint as numpy_randint
import bot.utils as utils

def roll_dice(command:str):
    """
    Roll a dice with a given amount of sides a give number of times 
    """

    output_data = ""
    
    # Handle the "help" command, return instructions
    items = command.split(" ")
    if len(items) == 2:
        if items[1] == "help":
            return ("Syntax help for the /roll command:\n"
                  + "The syntax is\n"
                  + "/roll <whole number>D<whole number>\n\n"
                  + "For instance: '/roll 3D8' is a valid input.\n"
                  + "You can also add a constant by doing this '/roll 5D6+13'.\n")
    
        
        # Just for funsies
        elif items[1] == "joint":
            return "Hierbij een bon voor een gratis JONKO!"
        
        elif items[1] == "rick":
            return utils.get_rickroll_text()
        
        
        # Splits the xDy into x and y, splitsing on the character 'D' (of 'd' for geklapte jonkos who can't follow basic instructions).
        items[1] = items[1].upper()
        amount, dice_size = utils.split_roll_data(items[1], "D")
        offset = 0
        if "+" in dice_size:
            dice_size, offset = dice_size.split("+")
            offset = int(offset)
        
        # Split and check if amount of rolls isn't absurdly high
        amount, dice_size = utils.parse_int(amount), utils.parse_int(dice_size)

        if dice_size <= 0:
            return "Dice size can't be less than or equals 0"
    
        # Generate array of random dicerolls
        total = 0
        if amount <= 10:
            rolls = numpy_randint(0, dice_size + 1, amount)
            total = sum(rolls)
            for i in range(amount):
                output_data += "Roll " + str(i + 1) + " = " + str(rolls[i]) + "\n"
            output_data += "\n"
        else:
            total = round(random.triangular(0,dice_size) * amount)
    
        output_data += "Total roll "
        if offset > 0:
            output_data += "with added bonus of " + str(offset) + " "
        output_data += "= " + str(total + offset)
        return output_data
    else:
        return "Add something to make it a valid command, or type '/roll help' for help"

# Command to generate a random DnD character (WIP-ish)
def create_character(command:str):
    
    items = command.split(" ")
    if len(items) == 2:
        if items[1] == "help":
            return ("Syntax help for the /create_character command:\n"
                  + "just use \'/create_character\'...")
    
    return ("Unfortunately, this hasn't been implemented yet.\n"
          + "As a substitude, go to\n"
          + "https://levi-blodgett.github.io/dnd-char-generator/#top\n"
          + "for a charactersheet randomizer.")