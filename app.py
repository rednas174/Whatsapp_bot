"""
Created on Fri Jan  8 15:39:32 2021

@author: Sander
"""


#==================================================================#
# TODO:                                                            #
#    +-> Add /poll                                                 #
#    +-> Add /WTFact                                               #
#    +-> fix the big F                                             #
#    +-> Emojify text (supercringe)                                #
#==================================================================#

from flask import Flask, request

import bot.handlers.dnd_handler as dnd_handler
import bot.handlers.misc_handler as misc_handler
import bot.handlers.poll_handler as poll_handler
import bot.utils as utils
import os

app = Flask(__name__)

# Main function called when the phone sends a request.
# Whatever is returned from this function is whatever will be send back to the phone.

# Variable for tracking the pipeline iterations
command_recursions = 0
def handle_command(command:str, sender:str):
    global command_recursions
    
    items = command.split(" ", 1)
    
    # Check for the necessity of recursion
    if len(items) == 2:
        if items[1][0] == "/":
            command_recursions += 1
            
            # A maximum of 100 recursions
            if command_recursions < 100:
                
                # re-evaluate the second part of the command, then replace the output with the current command and evaluate that.
                command = items[0] + " " + handle_command(items[1], sender)
            else:
                return "Recursion limit reached, sorry"
    
    try:
        if   command[:5]    == "/help":
            returned_message = misc_handler.get_help(command)
        
        elif command[:5]    == "/roll":
            returned_message = dnd_handler.roll_dice(command)
            
        elif command[:5]    == "/link": 
            returned_message = misc_handler.get_group_link(command)
    
        elif command[:17]   == "/create_character":
            returned_message = dnd_handler.create_character(command)
        
        elif command[:7]    == "/repeat":
            returned_message = misc_handler.get_repeated_command(command)
        
        elif command[:10]   == "/horoscope":
            returned_message = misc_handler.get_horoscope(command)

        elif command[:4]    == "/bms":
            returned_message = misc_handler.get_bms_script(command)

        elif command[:6]    == "/agree":
            returned_message = misc_handler.agree(command)

        elif command[:9]    == "/disagree":
            returned_message = misc_handler.disagree(command)
        
        elif command[:10]   == "/updatelog":
            returned_message = misc_handler.get_updates(command)
        
        elif command[:7]    == "/UwUify":
            returned_message = misc_handler.UwUify(command)
        
        elif command[:11]   == "/disclaimer":
            returned_message = misc_handler.get_disclaimer(command)
        
        elif command[:2]    == "/f":
            returned_message = misc_handler.F(command)
        
        elif command[:5]    == "/poll":
            if command_recursions > 0:
                return "Unfortunately, /poll is incompatible with recursive commands"
            else:
                returned_message = poll_handler.handle_poll(command, sender)
        
        elif command[:6]    == "/roast":
            returned_message = misc_handler.get_roast(command)
            
        elif command[:10]    == "/nicecock":
            returned_message = misc_handler.nice_cock(command)
            
            
        else: 
            returned_message = "_Error 404: Command '" + command + "' not found._"

    except Exception as e:
        print(e)
        return "Oops, something went wrong, type '/roll help' for info about the syntax"
    return returned_message


@app.route('/', methods=['POST'])
def result():
    global command_recursions
    command_recursions = 0
    
    returned_message = ""
    
    # Get metadata from message
    data_from_client = request.get_json()
    
    # Print the contents of the message
    print(">>>", data_from_client["senderMessage"][:100].replace("\n", " -"))
    
    returned_message = handle_command(data_from_client["senderMessage"], data_from_client['senderName'])
    
    return utils.gen_send_data(returned_message)
    
        
        
app.run(host = "0.0.0.0")
