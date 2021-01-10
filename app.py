"""
Created on Fri Jan  8 15:39:32 2021

@author: Sander
"""


#===============================================================#
# TODO:                                                         #
#   |                                                           #
#   +-> Fix /roll help formatting, it fucking sucks buttholes   #
#===============================================================#

# The app requires a specific message 
#{
#  "data":[
#      {
#       "message": "<Message here>"
#      }
#   ]
#}

from flask import Flask, request

import bot.handlers.dnd_handler as dnd_handler
import bot.handlers.misc_handler as misc_handler
import bot.utils as utils


app = Flask(__name__)

# Main function called when the phone sends a request.
# Whatever is returned from this function is whatever will be send back to the phone.
@app.route('/', methods=['POST'])
def result():
    
    # Get metadata from message
    data_from_client = request.get_json()
    
    # Print the contents of the message
    print(">>>", data_from_client["senderMessage"])
    
    try:
        # Because everyone keeps saying /help
        if data_from_client['senderMessage'][:5] == "/help":
            return misc_handler.get_help(data_from_client["senderMessage"])
        
        # Handle if the message comes from the /roll trigger
        elif data_from_client['senderMessage'][:5] == "/roll":
            return dnd_handler.roll_dice(data_from_client["senderMessage"])
            
        # Handle if the message comes from the /link trigger
        elif data_from_client['senderMessage'][:5] == "/link": 
            return misc_handler.get_group_link(data_from_client["senderMessage"])
    
        # Handle if the message comes from the /create_character trigger
        elif data_from_client['senderMessage'][:17] == "/create_character":
            return dnd_handler.create_character(data_from_client["senderMessage"])

    except Exception as e:
        print(e)
        return utils.gen_send_data("Oops, something went wrong, type '/roll help' for info about the syntax")
    return ""
        
        
app.run(host = "0.0.0.0")
