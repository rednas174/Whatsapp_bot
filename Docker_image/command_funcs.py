# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 15:39:32 2021

@author: Sander
"""

import json
import random
import re


# Split the command on a character and always return an array with at least length 2
def split(command:str, character:str):
    
    items = command.split(character)
    if len(items) == 1:
        items.append("")
    return items


def parseInt(to_convert:str):
    """Converts a string to an integer with the
    given base. If base is None and the string starts
    with a 0, automatically resolve the given base.

    Supported bases are:
    - 0x: Hexadecimal
    - 0o or 0: Octal

    The rest is interpreted as base 10.

    Args:
        to_convert (string): The string to convert to an int.
        base (int, optional): Assume to_convert is in this base. If none, get the base from the string. Defaults to None.

    Raises:
        ValueError: If to_convert cannot be converted.

    Returns:
        int: The converted integer.
    """
    
    to_convert = to_convert.lower()
    
    # Determine which system this uses
    if re.match("0x.*", to_convert):
        base = 16

    elif re.match("0b.*", to_convert):
        base = 2
    
    elif re.match("0o.*", to_convert):
        base = 8
    
    else:
        base = 10

    # Try to convert the number.
    return int(to_convert, base)


def splitRollData(data:str, delim:str = "D"):
    """This function splits the roll data on the
    amount of throws and the number of die sides.

    It does this by splitting at the first encountered D,
    unless the first number is in base 16 (hex). If it is,
    it takes the last D of this number as split. This means
    that it stops before the 2nd number notation.

    /roll 5D8: No hexadecimal, first D matched. Returns ("5", "8",).
    /roll 0xDD8: Hexadecimal, last D matched. Returns ("0xD", "8",).
    /roll 5D0xDD: No hexadecimal, first D is matched. Returns ("5", "0xDD",).
    /roll 0xDD0xDD: Hexadecimal, last D matched before 2nd base. Returns ("0xD", "0xDD",).

    Args:
        data (str): The argument passed to /roll. For example 1D0xDD.
    """

    split_last: bool = False

    # Check if the first part is in hexadecimal.
    # If so, split on the last D 
    if len(data) > 1 and data[:2] == "0x":
        split_last = True
    
    # Keep reading and appending to the result strings
    # until what is described above.
    split_index: int = -1
    for i, character in enumerate(data):
        # We stop at the first case we encounter the delimiter.
        if character == delim and split_index < 0 and not split_last:
            split_index = i
            break

        # Continue until the 2nd digit or the last D.
        elif character == delim and split_last:
            split_index = i
        
        # Check if the next part of the string is a new number,
        # break if that is the case.
        if len(data) > i + 3 and data[i + 1:i + 3] == "0x":
            break

    # Skip the D and return the two halves.
    return data[:split_index], data[split_index + 1:],


def genSendData(data:str):
    """This function converts the given data to a JSON
    string that can be passed to WhatsApp to send a message.

    Args:
        data (string): The message to be sent.
    """

    message_data = {
        "data": [
            {
                "message": data,
            },
        ]
    }

    return(json.dumps(message_data))


# Command to roll dice
def command_roll(command:str):
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
    amount, dice_size = splitRollData(items[1], "D")
    offset = 0
    if "+" in dice_size:
        dice_size, offset = dice_size.split("+")
        offset = int(offset)
    
    # Split and check if amount of rolls isn't absurdly high
    amount, dice_size = parseInt(amount), parseInt(dice_size)
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
def command_link(command:str):
    
    items = split(command, " ")
    if items[1] == "help":
        return genSendData("Syntax help for the /link command:\n"
                         + "just use \'/link\'...\n"
                         + "Out of sheer spite I will make you retype the command\n"
                         + ">:D\n")
    return genSendData("https://chat.whatsapp.com/L2xVHEBzWDM0cXWjif8TDf")



# Command to generate a random DnD character (WIP-ish)
def command_create_character(command:str):
    
    items = split(command, " ")
    if items[1] == "help":
        return genSendData("Syntax help for the /create_character command:\n"
                         + "just use \'/create_character\'...")
    return genSendData("Unfortunately, this hasn't been implemented yet.\n"
                     + "As a substitude, go to\n"
                     + "https://levi-blodgett.github.io/dnd-char-generator/#top\n"
                     + "for a charactersheet randomizer.")



# Command to get all available commands.
def command_help(command:str):
    
    return genSendData("Current commands available:\n"
                     + "/create_character\n"
                     + "/help\n"
                     + "/link\n"
                     + "/roll\n"
                     + "Add \'help\' after a command to get the syntax.")