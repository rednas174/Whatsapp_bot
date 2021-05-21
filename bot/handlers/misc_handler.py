from bs4 import BeautifulSoup
import urllib3
import datetime
import random

# If someone wants to impersonate and fake a horoscope website, I'm fine with it tbh
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

horoscopes = {"ARIES": 1, "TAURUS": 2, "GEMINI": 3, "CANCER": 4, "LEO": 5, "VIRGO": 6, "LIBRA": 7, "SCORPIO": 8, "SAGITTARIUS": 9, "CAPRICORN": 10, "AQUARIUS": 11, "PISCES": 12}
cached_horoscopes = {"ARIES": '', "TAURUS": '', "GEMINI": '', "CANCER": '', "LEO": '', "VIRGO": '', "LIBRA": '', "SCORPIO": '', "SAGITTARIUS": '', "CAPRICORN": '', "AQUARIUS": '', "PISCES": ''}
UwUs = ["UwU", "OwO", ">w<", "^w^", "°w°", ";w;"]
insults = ["I'd like to roast you, but it looks like God already did.","You look like someone set your face on fire and then put it out with a hammer.","The only thing attracted to you is gravity","You’re not good looking enough to be a model, but you’re not smart enough to be anything else","If you’d like to know what sexual position produces the ugliest babies, you should ask your mother.","Can you speak a little louder? I can’t hear you over the sound of how stupid you are.","Why are you even talking to me? So your self esteem can match your IQ?","I’m not insulting you, I’m describing you.","If you hide your big nose and shut your big mouth, people will think you are attractive and well-spoken.","I guess God’s just making anybody these days.","You're so ugly, when your mom dropped you off at school she got a fine for littering.","Some babies were dropped on their heads but you were clearly thrown at a wall.","They say opposites attract. If that's so, you will meet someone who is good-looking, intelligent, and cultured.","I didn’t hear you. I’m busy ignoring an annoying person.","I don't know what your problem is, but I'll bet it's hard to pronounce.","Please excuse me while I transfer you to someone who speaks Fucktard.","It must take a lot of flexibility to fit your foot in your mouth and your head up your ass at the same time.","I don’t have the time nor the crayons to explain things to you","I’d love to keep chatting with you, but I’d rather have AIDS","I bet you swim with a t shirt on","You have all the charm and charisma of a burning orphanage","Your face is so oily that I’m surprised America hasn’t invaded yet.","If you were any dumber, someone would need to water you twice a week","If you were on fire and I had a cup of my own piss, I’d drink it","Do you still love nature, despite what it did to you?","The thing I dislike most about your face is that I can see it.","If B.S. was music, you’d be an orchestra.","You look like a before picture.","I’ve heard farts more intelligent than you.","You have a perfect face for radio.","They say that a million monkeys on a million typewriters will eventually produce the collected works of Shakespeare. If that theory is correct, I believe you will one day say something intelligent.","If you want to lose ten pounds of ugly fat, may I suggest you start with cutting off your head.","You look like somebody stepped on a goldfish.","I thought the trash got picked up last night, what are you still doing here?","Looking the way you do must save a lot of money on halloween.","I’d love to continue talking with you but my favorite commercial is on tv","I'd love to keep chatting with you, but right now I have to do literally anything else.","Did you get a bowl of soup with that haircut?","If you don’t like what I say about you, it would be a good idea to improve yourself.","Does being that ugly require a license?","You could throw a rock at the ground and miss","There’s no one in this world like you. Or at least I hope so.","You look like a man, and you need to lose some weight.","Did you cancel your barbecue?  Because your grill is messed up","Some people make millions.  You make memes.","Did you forget to wipe or is that your natural scent?","I missed you this week, but my aim is improving.","I'm surprised you've made it this far without being eaten.","Your body looks like your head is inflating a water balloon.","Your mother was a hamster.","How do you make an idiot wait?","If balls were dynamite, you wouldn't have enough to kill a fish.","I'd like to roast you, but I'm too busy judging your choices.","You are the worst part of everybody's day.","If your face were scrambled it would improve your looks.","I hope you don't feel the way you look.","In the book of Who's Who, you are listed as What's That?","It's surprising to me that a pig's bladder on a stick has gotten so far in life.","Sorry.  I'm on the toilet and I can only deal with one shit at a time.","If you fell into a river it would be unfortunate, but if anyone pulled you out it would be a disaster.","You are the discount version of whatever celebrity you look like.","When you go to the dentist, he needs anaesthetic.","You suck dick for bus fare and then walk home.","The fact that you are still alive is evidence that natural disasters are poorly distributed.","You are so dumb you can't fart and chew gum at the same time.","I was going to give you a nasty look, but I see you already have one.","Me think'st thou are a general offence and every man should beat thee.","I don't try to explain myself to idiots like you.  I'm not the Fucktard Whisperer.","Your mom circulates like a public key, servicing more requests than HTTP.","Your mom is so fat and dumb, the only reason she opened her email is because she heard it contained spam.","Your mom is so fat, she has to iron her pants in the driveway.","Your face invites a slap.","The only way you could get laid is if you crawled up a chicken's ass and waited."]

def get_help(command: str):
    """
    Returns:
        List of available bot commands
    """
    return ("*Current commands available:*\n"
          + "/create_character\n"
          + "/help\n"
          + "/link\n"
          + "/roll\n"
          + "/repeat\n"
          + "/horoscope\n"
          + "/bms\n"
          + "/agree\n"
          + "/disagree\n"
          + "/updatelog\n"
          + "/UwUify\n"
          + "/f\n"
          + "/disclaimer\n"
          + "/nicecock\n"
          + "/why\n"
          + "/nicecock"
          + "_Add 'help' after a command to get the syntax._")


def get_group_link(command: str):
    """
    Get the group-invite link for the grasmaaier chat
    """
    items = command.split(" ")
    
    # Handle help command
    if len(items) == 2:
        if items[1] == "help":
            return ("*Syntax help for /link:*\n"
                  + "just use \'/link\'...\n"
                  + "Out of sheer spite I will make you retype the command\n"
                  + ">:D\n")
    return "https://chat.whatsapp.com/L2xVHEBzWDM0cXWjif8TDf"


def get_horoscope(command: str):
    """
    Functionality:
        Gets the current horoscope.
        
    args:
        command: The given command, should be /horoscope [horoscope sign]

    Returns:
        String with response to client.
    """
    items = command.split(" ")
    
    # Handle help command
    if len(items) == 2:
        if items[1] == "help":
            return ("*Syntax help for /horoscope:*\n"
                  + "Simply add your sign after the command\n"
                  + "Example: '/horoscope pisces'.")
        items[1] = items[1].upper()
        try:
            if cached_horoscopes[items[1]]:
                
                # Check if the horoscope is still up to date
                cur_month = datetime.datetime.now().strftime("%B")[:3]
                cur_day   = datetime.datetime.now().day
                cur_year  = datetime.datetime.now().year
                
                cur_date = str(cur_month) + " " + str(cur_day) + " " + str(cur_year)
                cached_horoscope_date = cached_horoscopes[items[1]].split("-")[0][:-1].replace(",", "")
                
                # If it is, no need to get it again
                if cur_date == cached_horoscope_date:
                    print("[LOG] Using cached horoscope")
                    return cached_horoscopes[items[1]]
            
            
            print("[LOG] Getting horoscope")
            # Implicit else: Get current horoscope
            
            # Prepare variables for later use
            chosen_horoscope = items[1]
            horoscope_index = horoscopes[chosen_horoscope]
            
            # Get the current horoscope of the specified sign
            http = urllib3.PoolManager()
            url = 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=' + str(horoscope_index)
            response = http.request('GET', url)
            soup = BeautifulSoup(response.data, features="html.parser")
            t = soup.get_text()
            
            # Extract horoscope from entire page
            horoscope = t[t.find("Monthly\n")+44:t.find("\n", t.find("Monthly\n")+45)]
            
            # Cache horoscope for later use, the website thanks me
            cached_horoscopes[chosen_horoscope] = horoscope
            
            return horoscope
                
        except KeyError:
            return "Sorry, but it seems like that wasn't a valid horoscope option ;("
    else:
        return "Oops, you need to (only) add your zodiac sign for this to work."
    
    
def get_repeated_command(command: str):
    """
    Functionality:
        Repeats a given string.
        Out of precaution, " " are put around the string to make sure the
        text always has at least some context. Maybe this is a bit too much,
        but for the time being, this is how it is.
        
    Parameters:
        command: The given command to be repeated

    Returns:
        string to the client
    """
    items = command.split(" ", 1)
    if len(items) == 2:
        if items[1] == "help":
            return ("*Syntax help for /repeat:*\n"
                  + "Repeats the text you give it.\n"
                  + "\n"
                  + "Currently, it has a limit of 10.000 characters, and adds \" at the beginning and end.\n"
                  + "Example '/repeat test'")
        else:
            return "\"" + items[1] + "\""
    else:
        return "Just add some text after the command you clapped jonko >:("


def get_bms_script(command: str):
    items = command.split(" ")
    
    # Handle help command
    if len(items) == 2:
        if items[1] == "help":
            return ("*Syntax help for /bms:*\n"
                  + "Just use '/bms'...\n"
                  + "\n"
                  + "Like, there's nothing else this command could possibly do except send the bee movie script :/")
        
    elif len(items) == 1:
        # Open the file and send the contents back
        f = open("./bot/bee_movie_script.txt", 'r')
        script = f.read()
        f.close()
        return script
    
    elif len(items) == 8:
        # Just a fun easter egg ;)
        return "Oh look who has checked the code ;)"
    
    else:
        return "_Error in the syntax (/bms)_"
    

def agree(command: str):
    items = command.split(" ")
    
    # Handle help command
    if len(items) == 2:
        if items[1] == "help":
            return ("*Syntax help for /agree:*\n"
                  + "agrees wit whatever you said\n"
                  + "Example: '/agree'.")
        else:
            return "_Error in the syntax (/agree)_"
        
    elif len(items) == 1:
        return ("Yes, you are _objectively_ right my friend.\n"
              + "Not even science could ever hope to achieve the impossibility that is proving you wrong :)")
    
    else:
        return "_Error in the syntax_"


def disagree(command: str):
    items = command.split(" ", 1)
    
    # Handle help command
    if len(items) == 2:
        if items[1] == "help":
            return ("*Syntax help for /disagree:*\n"
                  + "Disagrees with the person you specify\n"
                  + "Example: '/disagree GeklapteJonko'.")
        else:
            return "Oh boi, " + items[1] + " is a complete fucking idiot, this is outrageous. How can someone with such low intelligence even normally eat without choking to death?????"
    
    elif len(items) == 1:
        return "Oh boi, this is completely fucking idiotic and outrageous. How can someone with such low intelligence even normally eat without choking to death?????"
    
    else:
        return "_Error in the syntax (/disagree)_"


def get_updates(command: str):
    items = command.split(" ", 1)
    
    # Handle help command
    if len(items) == 2:
        if items[1] == "help":
            return ("*Syntax help for /updatelog:*\n"
                  + "Shows the latest updates, no need to add anything after.\n"
                  + "Example: '/updatelog'.")
    
    #handle log request
    elif len(items) == 1:
        return ("*Latest updates:*\n"
              + "_Added the following commands:_\n"
              + "/nicecock\n"
              + "\n"
              + "_Changed the functionality of the following commands:_\n"
              + "- ")


def UwUify(command: str):
    items = command.split(" ", 1)
    if len(items) == 2:
        if items[1] == "help":
            return ("*Swyntax hewp for /UwUify: >w<*\n"
                  + "Impwoves da twext to UwU wangwuage OwO\n"
                  + "Exwampwe: '/UwUify This is normal text' UwU.")
        else:
            
            # Generic cursifiers
            items[1] = items[1].replace("th", "d")
            items[1] = items[1].replace("r", "w")
            items[1] = items[1].replace("l", "w")
            items[1] = items[1].replace("is", "ish")
            items[1] = items[1].replace("te", "twe")
            
            # 1 out of every 5 dot enters become cursed
            for i in range(len(items[1])):
                if random.randint(1,2) == 1:
                    if items[1][i:i+2] == ".\n":
                        items[1] = items[1][:i+1] + " " + UwUs[random.randint(0,len(UwUs)-1)] + items[1][i+1:] + " >w<"
            return items[1]
    else:
        return "Ewwow in de swyntax >w<"


def F(command: str):
    items = command.split(" ", 1)
    if len(items) == 2:
        if items[1] == "help":
            return ("*Syntax for /f:*\n"
                  + "A beautiful F")
        else:
            return "_Error in the syntax (/f)_"
    if len(items) == 1:
        return ("⠀⠀⠀⢀⡤⢶⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    \n"
              + "⠀⠀⢀⣠⣤⣤⣤⣿⣧⣀⣀⣀⣀⣀⣀⣀⣀⣤⡄⠀  \n"
              + "⢠⣾⡟⠋⠁⠀⠀⣸⠇⠈⣿⣿⡟⠉⠉⠉⠙⠻⣿⡀  \n"
              + "⢺⣿⡀⠀⠀⢀⡴⠋⠀⠀ ⣿⣿⡇⠀⠀⠀⠀⠀⠙⠇  \n"
              + "⠈⠛⠿⠶⠚⠋⣀⣤⣤⣤⣿⣿⣇⣀⣀⣴⡆     \n"
              + " ⠀  ⠀⠀⠀⠠⡞⠋⠀⠀⠀⣿⣿⡏⠉⠛⠻⣿⡀     \n"
              + "   ⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣿⣿⡇⠀⠀⠀⠈⠁⠀⠀   \n"
              + "   ⠀ ⠀⣠⣶⣶⣶⣶⡄⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀   \n"
              + "   ⠀ ⢰⣿⠟⠉⠙⢿⡟⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀   \n"
              + "   ⠀ ⢸⡟⠀⠀⠀⠘⠀⠀⠀⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀   \n"
              + "   ⠀ ⠈⢿⡄⠀⠀⠀⠀⠀⣼⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀   \n"
              + "   ⠀ ⠀⠀⠙⠷⠶⠶⠶⠿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀   \n")
    
    else:
        return "_Error in the syntax (/f)_"

def get_disclaimer(command: str):
    items = command.split(" ", 1)
    if len(items) == 2:
        if items[1] == "help":
            return ("*Syntax for /disclaimer:*\n"
                  + "Get the disclaimer from the license\n"
                  + "Example: /disclaimer\n"
                  + "It's simple.")
        else:
            return "_Error in the syntax (/disclaimer)_"
    
    elif len(items) == 1:
        f = open("./README.md", 'r')
        text = f.read()
        f.close()
        start_index = text.find("## License")+12
        end_index   = text.find("\n\n", start_index)
        return "*Disclaimer using this bot*\n\n" + text[start_index:end_index]
    
    else:
        return "_Error in the syntax_"


def get_roast(command:str):
    items = command.split(" ", 1)
    if len(items) == 2:
        if items[1] == "help":
            return ("*Syntax for /roast:*\n"
                  + "Roast someone else\n"
                  + "Example: /roast\n"
                  + "It's really simple.")
        else:
            return "_Error in the syntax_"
    
    elif len(items) == 1:
        chosen = random.randint(0,len(insults)-1)
        return insults[chosen]
    
    else:
        return "_Error in the syntax (/roast)_"


def nice_cock(command: str):
    items = command.split(" ", 1)
    if len(items) == 2:
        if items[1] == "help":
            return ("*Syntax for /nicecock:*\n"
                  + "A compliment for your cock")
        else:
            return "_Error in the syntax (/nicecock)_"
    if len(items) == 1:
        return """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⢿⣿⣿⠿⠛⠿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠉⠄⣀⡤⢤⣤⣈⠁⣠⡔⠶⣾⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠛⠋⠁⠄⠄⠄⣼⣿⠁⡀⢹⣿⣷⢹⡇⠄⠎⣿
⣿⣿⣿⠿⠛⠉⠁⠄⠄⠄⠄⠄⠄⠄⠹⣇⣀⣡⣾⣿⡿⠉⠛⠒⠒⠋
⡿⠋⠁⠄⠄⢀⣤⣤⡀⠄⠄⠄⠄⠄⠄⠈⠙⠛⠛⠉⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⢹⣧⡈⠿⣷⣄⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣠
⠄⠄⠄⠄⠄⠈⠻⢿⣶⣌⣙⡛⠛⠿⠶⠶⠶⠶⠶⠖⣒⣒⣚⣋⡩⢱
⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠛⠛⠛⠻⠿⠿⠟⠛⠛⠛⠉⢉⣥⣶⣾⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠒⠶⣿⣿⣿⣿⣿⣿
⡟⠛⢻⣿⡟⠛⣿⡟⠛⠛⠛⠛⢻⣿⡿⠛⠛⠛⢻⡟⠛⠛⠛⠛⢻⣿
⡇⠄⠄⢻⡇⠄⣿⣿⣿⠄⠄⣿⣿⡏⠄⣼⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿
⡇⠄⣧⠄⠄⠄⣿⣿⣿⠄⠄⣿⣿⡇⠄⣿⣿⣿⣿⡇⠄⣥⣥⣥⣿⣿
⡇⠄⣿⣧⠄⠄⣿⡟⠛⠄⠄⠛⢻⣷⣄⠈⠙⠛⢹⡇⠄⠉⠉⠉⢹⣿
⣿⡿⠛⠛⠛⢻⣿⠿⠛⠛⠛⢿⣿⣿⡿⠛⠛⠛⢻⡟⠛⣿⡿⠛⣻⣿
⡟⠄⣼⣿⣿⣿⡇⠄⣾⣿⣧⠄⢻⡏⠄⣼⣿⣿⣿⡇⠄⡟⢀⣴⣿⣿
⡇⠄⣿⣿⣿⣿⡄⠄⣿⣿⣿⠄⢸⡇⠄⣿⣿⣿⣿⡇⠄⣀⠈⢻⣿⣿
⣿⣄⠈⠙⠛⢻⣧⡄⠙⠛⠉⣠⣿⣷⣄⠈⠙⠛⢹⡇⠄⣿⣧⠄⠻⣿
"""
    
    else:
        return "_Error in the syntax (/nicecock)_"

def why(command: str):
    items = command.split(" ", 1)
    if len(items) == 2:
        if items[1] == "help":
            return ("*Syntax for /why:*\n"
                  + "Just crying out why anyone would do this ;(")
        else:
            return "_Error in the syntax (/why)_"
    if len(items) == 1:
        return """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠀⠀⠠⠀⠀⠀⠀⠀⣀⡀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠂⠁⠀⠀⠀⠀⠀⠁⠢⡄⠉⠀⠀⠀⠈⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡈⠀⠀⠴⠖⠉⠁⠀⠉⠑⠶⢿⠄⠲⠶⠶⠶⠠⠤⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠌⠀⠀⠀⠀⠀⣀⣤⣲⠸⠿⠿⠏⣛⣤⣠⣄⣖⠒⠒⢒⣚⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠔⠸⠇⠀⠀⢠⠀⠹⠗⠉⡁⠠⣀⣦⣀⠀⠉⠨⠁⠂⢐⡶⣶⣖⠚⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠈⠉⢉⣉⢀⠀⣾⡷⣏⣹⣇⢤⣀⣀⠀⣿⣻⣯⡽⠦⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠚⠛⠛⢛⣷⠎⠋⢀⡀⠀⠀⠀⡀⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠖⠊⠁⠀⠀⠀⠀⠈⠛⠉⠉⠈⢄⠀⠀⠀⠀⠀⢠⢄⡀⠀⠀⠀
⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⡀⠀⢸⡙⣦⢻⣟⢦⠀
⠀⠀⠇⠀⠀⠀⠀⠀⠀⠀⣴⠉⠥⠬⡭⢈⣉⠐⠒⠢⠶⠦⠀⠀⠀⠰⠦⠒⠋⠁⠀⢻⣧⠀⢣⢻⡎⡏⡼⠀
⠀⠀⠐⠄⠀⠀⠀⠀⠀⢦⡙⠶⠶⠶⠂⠤⠄⣉⣉⣤⣶⣿⣻⢿⠛⠛⠒⢈⠹⠀⢀⣠⠏⠓⠃⠀⢀⡸⠁⠀
⠀⠀⠠⠼⣦⣤⣀⠀⠀⠀⠉⠃⠀⠀⠀⠀⢰⣤⡞⢹⢱⣋⡏⡼⣾⣗⠁⠀⢀⡞⠁⠀⠀⠀⣠⠖⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠓⠯⠵⣒⣒⠴⠶⠆⠠⠤⢼⡾⠇⠈⠀⠙⠃⠗⠋⡼⠀⠀⢸⠀⠀⠀⠒⡎⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⢹⡗⠦⠤⢀⣤⠖⢏⡀⠀⠀⠀⢇⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⡏⠀⠀⠙⢦⠀⠀⠘⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀
"""
    
    else:
        return "_Error in the syntax (/why)_"











