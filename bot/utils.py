import json

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