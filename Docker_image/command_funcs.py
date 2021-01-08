# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 15:39:32 2021

@author: Sander
"""

import random

# Part 2 of necessary message       
dummyStr_1 = """\"
      }
   ]
}"""

# Part one of necessary message
dummyStr = """{
  "data":[
      {
       "message":\""""
       

# Part 2 of necessary message       
dummyStr_1 = """\"
      }
   ]
}"""


# Split the command on a character and always return an array with at least length 2
def split(command, character):
    items = command.split(character)
    if len(items) == 1:
        items.append("")
    return items


# Sandwich the message between the JSON code thingies
def genSendData(data):
    return(dummyStr + data + dummyStr_1)


# Command to roll dice
def command_roll(command):
    output_data = ""
    
    # Handle the "help" command, return instructions
    items = split(command, " ")
    if items[1] == "help":
        return genSendData("Syntax help for the /roll command:\n"
                         + "The syntax is\n"
                         + "/roll <whole number>D<whole number>\n\n"
                         + "For instance: '/roll 3D8' is a valid input.\n"
                         + "You can also add a constant by doing this '/roll 5D6+13'.\n")

    # Just for funsies
    elif items[1] == "joint":
        return genSendData("Hierbij een bon voor een gratis JONKO!")
    
    # Splits the xDy into x and y, splitsing on the character 'D' (of 'd' for geklapte jonkos who can't follow basic instructions).
    items[1] = items[1].upper()
    amount, dice_size = items[1].split("D")
    offset = 0
    if "+" in dice_size:
        dice_size, offset = dice_size.split("+")
        offset = int(offset)
    
    # Split and check if amount of rolls isn't absurdly high
    amount, dice_size = int(amount), int(dice_size)
    if amount > 10000:
        return genSendData("Sorry, but this is too many dice rolls...")

    # Roll x amount of dice with size y
    total = 0
    rolls = []
    for i in range(0,amount):
        current_roll = random.randint(1,int(dice_size))
        if i < 10:
            rolls.append(current_roll)
        total += current_roll

    # If the amount of thrown dice is larger than 10, only output the total
    if amount <= 10:
        for i in range(amount):
            output_data += "Roll " + str(i + 1) + " = " + str(rolls[i]) + "\n"
        output_data += "\n"
    
    output_data += "Total roll "
    if offset > 0:
        output_data += "with added bonus of " + str(offset) + " "
    output_data += "= " + str(total + offset)
    return (genSendData(output_data))


# Command to get the link of the Grasmaaier fanclub whatsapp group
def command_link(command):
    items = split(command, " ")
    if items[1] == "help":
        return genSendData("Syntax help for the /link command:\n"
                         + "just use \'/link\'...\n"
                         + "Out of sheer spite I will make you retype the command\n"
                         + ">:D\n")
    return genSendData("https://chat.whatsapp.com/L2xVHEBzWDM0cXWjif8TDf")


# Command to generate a random DnD character (WIP-ish)
def command_create_character(command):
    items = split(command, " ")
    if items[1] == "help":
        return genSendData("Syntax help for the /create_character command:\n"
                         + "just use \'/create_character\'...")
    return genSendData("Unfortunately, this hasn't been implemented yet.\n"
                     + "As a substitude, go to\n"
                     + "https://levi-blodgett.github.io/dnd-char-generator/#top\n"
                     + "for a charactersheet randomizer.")


# Command to get all available commands.
def command_help(command):
    return genSendData("Current commands available:\n"
                     + "/create_character\n"
                     + "/help\n"
                     + "/link\n"
                     + "/roll\n"
                     + "Add \'help\' after a command to get the syntax.")