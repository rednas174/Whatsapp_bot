"""
Created on Fri Jan  8 15:39:32 2021

@author: Sander
"""


#==================================================================#
# TODO:                                                            #
#   |                                                              #
#   +-> Add /UwUify and /updatelog                                 #
#==================================================================#

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
    print(">>>", data_from_client["senderMessage"][:100].replace("\n", " -"))
    
    if len(data_from_client["senderMessage"]) > 10000:
        return "Suck a huge fat cock, I'm not gonna repeat some _*huge mega uber triple style ginormous*_ bullshit spam"
    
    try:
        if data_from_client['senderMessage'][:5] == "/help":
            return utils.gen_send_data(misc_handler.get_help(data_from_client["senderMessage"]))
        
        elif data_from_client['senderMessage'][:5] == "/roll":
            return utils.gen_send_data(dnd_handler.roll_dice(data_from_client["senderMessage"]))
            
        elif data_from_client['senderMessage'][:5] == "/link": 
            return utils.gen_send_data(misc_handler.get_group_link(data_from_client["senderMessage"]))
    
        elif data_from_client['senderMessage'][:17] == "/create_character":
            return utils.gen_send_data(dnd_handler.create_character(data_from_client["senderMessage"]))
        
        elif data_from_client['senderMessage'][:7] == "/repeat":
            return utils.gen_send_data(misc_handler.get_repeated_command(data_from_client['senderMessage']))
        
        elif data_from_client['senderMessage'][:10] == "/horoscope":
            return utils.gen_send_data(misc_handler.get_horoscope(data_from_client['senderMessage']))

        elif data_from_client['senderMessage'][:4] == "/bms":
            return utils.gen_send_data(misc_handler.get_bms_script(data_from_client['senderMessage']))

        elif data_from_client['senderMessage'][:6] == "/agree":
            return utils.gen_send_data(misc_handler.agree(data_from_client['senderMessage']))

        elif data_from_client['senderMessage'][:9] == "/disagree":
            return utils.gen_send_data(misc_handler.disagree(data_from_client['senderMessage']))
        
        elif data_from_client['senderMessage'][:10] == "/updatelog":
            return utils.gen_send_data(misc_handler.get_updates(data_from_client['senderMessage']))
        
        elif data_from_client['senderMessage'][:7] == "/UwUify":
            return utils.gen_send_data(misc_handler.UwUify(data_from_client['senderMessage']))

    except Exception as e:
        print(e)
        return utils.gen_send_data("Oops, something went wrong, type '/roll help' for info about the syntax")
    return ""
        
        
app.run(host = "0.0.0.0")
