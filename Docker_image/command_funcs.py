# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 15:39:32 2021

@author: Sander
"""

import json
import random


# Split the command on a character and always return an array with at least length 2
def split(command, character):
    items = command.split(character)
    if len(items) == 1:
        items.append("")
    return items


def parseInt(to_convert, base=None):
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

    # Check if a base representation is given in the string
    # and it is requested that we auto determine the base.
    if base is None and len(to_convert) > 1 and to_convert[0] == "0":
        # Hexadecimal.
        if to_convert[1].lower() == "x":
            base = 16
        
        # Octal.
        else:
            base = 8
    
    # Otherwise we assume the base is 10.
    else:
        base = 10

    # Try to convert the number.
    return int(to_convert, base)


def genSendData(data):
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