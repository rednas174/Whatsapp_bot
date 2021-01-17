# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:43:21 2021

@author: Sander
"""

import random

# TODO: '/poll vote 88' has no output
#     : invalid poll id gives no output


# Poll datastructure
# 
# {
#   "number or name of person":
#       {
#           "__name"   : name,
#           "__votees" : 
#               [
#                   ["votee", "option"],
#                   ["votee", "option"],
#                   ["votee", "option"],
#                   ...
#               ]
#           "__id"     : unique id for every poll
#           "Option 1" : votes,
#           "Option 2" : votes,
#           "Option 3" : votes,
#           ...
#       },
#
#  "number or name of person":
#       {
#           "__name"   : name,
#           "__votees" : 
#               [
#                   ["votee", "option"],
#                   ["votee", "option"],
#                   ["votee", "option"],
#                   ...
#               ]
#           "__id"     : unique id for every poll
#           "Option 1" : votes,
#           "Option 2" : votes,
#           "Option 3" : votes,
#           ...
#       },
#
#       ...
# }

# List of possible commands:
#   /poll create <name with spaces> [<options 1>/<option 2>/...]
#   >>> Creates a poll with that name in that persons account name
#   >>> A poll can't have these '-[]/' characters in either its name nor its options.
#   >>> Neither can a poll have __name of __votees as an option.
#
#   /poll remove
#   >>> Removes the poll associated with that person 
# 
#   /poll vote <name> -<option>
#   >>> Adds a vote to that poll.
#   --> Check if person already voted.




# TODO: Check if the voter votes for an existing option

polls = {}


def is_option(poll_id: str, option: str):
    if option[:2] == "__":
        return False
    
    for name in polls:
        if polls[name]["__id"] == int(poll_id):
            if option in list(polls[name]):
                return True
            else:
                return False
    
    return False


def vote(poll_id, person, option):
    
    # Loop over every poll until the ID matches
    for poll_option in polls:
        if polls[poll_option]["__id"] == int(poll_id):
            
            # Loop over every vote until the voter has been found
            for voter_index in range(len(polls[poll_option]["__votees"])):
                
                # Change the vote, or return a sassy message
                if polls[poll_option]["__votees"][voter_index][0] == person:
                    
                    # Check if the votes votes again for the same
                    if polls[poll_option]["__votees"][voter_index][1] == option:
                        return "Can't vote for the same item twice, you clapped jonko"

                    else:
                        polls[poll_option][polls[poll_option]["__votees"][voter_index][1]] -= 1
                        polls[poll_option][option]   += 1
                        polls[poll_option]["__votees"][voter_index][1] = option
                        return "Changed vote"
            
            polls[poll_option]["__votees"].append([person, option])
            polls[poll_option][option] += 1
            return show_poll_by_id(int(poll_id))



def id_generator(name):
    loop = True
    while loop:
        new_id = random.randint(1,999)
        loop = False
        for poll_name in polls:
            if poll_name != name:
                if polls[poll_name]["__id"] == new_id:
                    loop = True
                    break
    return new_id


def create_poll(command, poll_creator):
    if command.count("[") == 1 and command.count("]") == 1:
        
        # Extract the poll name
        name = command.split(" ", 2)[-1]
        name = name[:name.find("[")]
        
        # Remove last space if present
        name = name[:-1] if name[-1] == " " else name
        
        # Extract the options
        options = command[command.find("[")+1:command.find("]")].split("/")
        
        for option in options:
            if option[:2] == "__":
                return "Error: You can't start a poll option with '__', please follow the "
        
        try:
            polls.pop(poll_creator)
        except:
            pass
        
        # Set default values
        poll_id = id_generator(poll_creator)
        
        polls[poll_creator] = {}
        polls[poll_creator]["__id"] = poll_id
        polls[poll_creator]["__name"] = name
        polls[poll_creator]["__votees"] = []
        
        # Insert options
        for option in options:
            polls[poll_creator][option] = 0
        
        return show_poll_by_id(poll_id)



def vote_poll(command, poll_votee):
    try:
        command = command.split(" ", 2)[-1]
        print(command)
        poll_id, option = command.split(" ", 1)
        
        
        
        for poll_name in polls:
            #print("id->", polls[poll_name]["__id"], int(poll_id))
            if polls[poll_name]["__id"] == int(poll_id):
                if is_option(poll_id, option):
                    return vote(poll_id, poll_votee, option)
                else:
                    return "Error: " + option + " isn't an option"
        
    except:
        return "Something went wrong, please make sure you follow the syntax of the command as described in '/poll help'"



def show_poll_by_id(ID):
    for poll_item in polls:
        if polls[poll_item]["__id"] == ID:
            out = "*Poll by " + poll_item + " (" + str(polls[poll_item]["__id"]) + "): " + polls[poll_item]["__name"] + "*\n\n"
            for option in list(polls[poll_item].keys()):
                if option[:2] != "__":
                    out += "_" + option + "_ with " + str(polls[poll_item][option]) + " vote(s)\n"
            return out
    return "Error 404: Poll not found"



def get_poll_list():
    out = "*List of all currently active polls:*\n\n"
    for option in list(polls.keys()):
        out += option + " (" + str(polls[option]["__id"]) + ") - " + polls[option]["__name"][:100]
    return out



def handle_poll(command:str, person:str):
    """
    Functionality:
        This command can create a poll.
        /poll create Klap die jonko [Yes/No/Unsure what to do/NOOOO]

    Parameters
    ----------
    command: Whatever the command is
    creator: 
    
    Returns
    -------
    None.

    """
    items = command.split(" ")
    
    # Handle help command
    if len(items) == 1:
        return "You need to add something, perhaps 'help' to get the syntax help?"
    
    elif len(items) == 2:
        if items[1] == "help":
            return ("*Syntax help for /poll:*\n"
                  + "\n"
                  + "You can vote for or create a poll:\n"
                  + "\n"
                  + "_Creating a poll:_\n"
                  + "/poll create <name> [<option 1>/<option 2>/...]"
                  + "\n"
                  + "_Voting for a poll:_\n"
                  + "/poll vote <name> <option>\n"
                  + "\n"
                  + "Keep in mind that you need to follow the formatting, else there might be some naming problems."
                  + "You can also list all polls with their IDs with /poll list.\n"
                  + "then show it with /poll show <number or name (for special people ;)>")
        
        if items[1] == "list":
            return "".join("Poll (" + str(polls[x]["__id"]) + ") from: " + x[:100] + "\n\n" for x in list(polls.keys()))
        
    elif len(items) == 3:
        if items[1].lower() == "show":
            return show_poll_by_id(int(items[2]))
    
    else:
        if items[1].lower() == "create":
            return create_poll(command, person)
        if items[1].lower() == "vote":
            return vote_poll(command, person)
        else:
            return items[1] + " isn't a valid option"



if __name__ == "__main__":
    
    print("\n\n>" + handle_poll("/poll create Moet die jonko geklapt worden? [Ja/Nee/Im a loser]", "Prive"))
    
    print("\n\n>" + handle_poll("/poll list", "Prive"))
    
    print("\n\n>" + handle_poll("/poll show 111", "Prive"))
    
    print("\n\n>" + handle_poll("/poll vote 111 Ja", "Prive"))
    
    print("\n\n>" + handle_poll("/poll vote 111 Nee", "Prive"))
    
    print("\n\n>" + handle_poll("/poll vote 111 DSADSADSA", "Prive"))