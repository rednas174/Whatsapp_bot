import json
import re

def split_string(command:str, character:str):
    """
    Split incoming command on a character
    Returns:
        Array with at least length 2 containing the split command
    """
    items = command.split(character)
    if len(items) == 1:
        items.append("")
    return items


def split_roll_data(data:str, delim:str = "D"):
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


def parse_int(to_convert:str):
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


def gen_send_data(data:str):
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