import bot.utils as utils

def get_help(command:str):
    """
    Returns:
        List of available bot commands
    """
    return utils.gen_send_data("Current commands available:\n"
                     + "/create_character\n"
                     + "/help\n"
                     + "/link\n"
                     + "/roll\n"
                     + "Add \'help\' after a command to get the syntax.")


def get_group_link(command:str):
    """
    Get the group-invite link for the grasmaaier chat
    """
    items = utils.split_string(command, " ")
    if items[1] == "help":
        return utils.gen_send_data("Syntax help for the /link command:\n"
                         + "just use \'/link\'...\n"
                         + "Out of sheer spite I will make you retype the command\n"
                         + ">:D\n")
    return utils.gen_send_data("https://chat.whatsapp.com/L2xVHEBzWDM0cXWjif8TDf")
