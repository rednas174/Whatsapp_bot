
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
from command_funcs import command_roll, command_link, command_create_character, genSendData
app = Flask(__name__)

# Main function called when the phone sends a request.
# Whatever is returned from this function is whatever will be send back to the phone.
@app.route('/', methods=['POST'])
def result():
    
    # Get metadata from message
    data_from_client = request.get_json()
    
    # Print the contents of the message
    print(data_from_client["senderMessage"])
    
    try:
    # Handle if the message comes from the /roll trigger
        if data_from_client['senderMessage'][:5] == "/roll":
            return command_roll(data_from_client["senderMessage"])
    
        # Handle if the message comes from the /link trigger
        elif data_from_client['senderMessage'][:5] == "/link": 
            return command_link(data_from_client["senderMessage"])
    
        # Handle if the message comes from the /create_character trigger
        elif data_from_client['senderMessage'][:17] == "/create_character":
            return command_create_character(data_from_client["senderMessage"])

    except Exception as e:
        # Print the error, and move on. NO THIS DOES NOT BOTHER ME AT ALL.
        print(e)
        return genSendData("Oops, something went wrong, type '/roll help' for info about the syntax")
    return ""
        
        
app.run(host = "0.0.0.0")

    
    
