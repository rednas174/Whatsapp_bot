
#===============================================================#
# TODO:                                                         #
#   |                                                           #
#   +-> Call individual functions for better code readability   #
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





# Sandwich the message between the JSON code thingies
def genSendData(data):
    return(dummyStr + data + dummyStr_1)

from flask import Flask, request
import random
app = Flask(__name__)


# Main function called when the phone sends a request.
# Whatever is returned from this function is whatever will be send back to the phone.
@app.route('/', methods=['POST'])
def result():
    
    # Get metadata from message
    a = request.get_json()
    
    # Print the contents of the message
    print(a["senderMessage"])
    
    # Handle if the message comes from the /roll trigger ----------------------
    if a['receiveMessagePattern'][0] == "/roll":
        try:
            output_data = ""
            
            # Handle the "help" command
            items = a["senderMessage"].split(" ")
            if items[1] == "help":
                return genSendData("""Syntax help for the /roll command:
The syntax is /roll <whole number>D<whole number>
For instance: '/roll 3D8' is a valid input.
You can also add a constant by doing this '/roll 5D6+13'.""")

            if items[1] == "joint":
#                genSendData("Hierbij een bon voor een gratis JONKO!")
                return genSendData("Hierbij een bon voor een gratis JONKO!")

            # Splits the xDy into x and y, splitsing on the character 'D' (of 'd' for geklapte jonkos who can't follow basic instructions).
            items[1] = items[1].upper()
            amount, dice_size = items[1].split("D")
            offset = 0
            if "+" in dice_size:
                dice_size, offset = dice_size.split("+")
                offset = int(offset)
            amount, dice_size = int(amount), int(dice_size)

            # Roll x amount of dice size y
            total = 0
            rolls = []
            for i in range(0,amount):
                current_roll = random.randint(1,int(dice_size))
                if i < 10:
                    rolls.append(current_roll)
                total += current_roll

            # If the amount is larger than 10, only output the total
            if amount < 10:
                for i in range(amount):
                    output_data += "Roll " + str(i + 1) + " = " + str(rolls[i]) + "\n"
                output_data += "\n"
            
            output_data += "Total roll "
            if offset > 0:
                output_data += "with added bonus of " + str(offset) + " "
            output_data += "= " + str(total + offset)
            return (genSendData(output_data))
        
        except Exception as e:
            # Print the error, and move on. NO THIS DOES NOT BOTHER ME AT ALL.
            print(e)
            return genSendData("Oops, something went wrong, type '/roll help' for info about the syntax")
        
        
    # Handle if the message comes from the /create_character trigger ----------
    if a['receiveMessagePattern'][0] == "/create_character":
        #try:
        return (genSendData("""Unfortunately, this hasn't been implemented yet.
As a substitude, go to 
https://levi-blodgett.github.io/dnd-char-generator/#top
for a charactersheet randomizer"""))
    return ""
        
        
app.run(host = "0.0.0.0")

    
    
