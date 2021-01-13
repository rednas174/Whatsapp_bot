from bs4 import BeautifulSoup
import urllib3
import datetime

# If someone wants to impersonate and fake a horoscope website, I'm fine with it tbh
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

horoscopes = {"ARIES": 1, "TAURUS": 2, "GEMINI": 3, "CANCER": 4, "LEO": 5, "VIRGO": 6, "LIBRA": 7, "SCORPIO": 8, "SAGITTARIUS": 9, "CAPRICORN": 10, "AQUARIUS": 11, "PISCES": 12}
cached_horoscopes = {"ARIES": '', "TAURUS": '', "GEMINI": '', "CANCER": '', "LEO": '', "VIRGO": '', "LIBRA": '', "SCORPIO": '', "SAGITTARIUS": '', "CAPRICORN": '', "AQUARIUS": '', "PISCES": ''}


def get_help(command:str):
    """
    Returns:
        List of available bot commands
    """
    return ("*Current commands available:(\n"
          + "/create_character\n"
          + "/help\n"
          + "/link\n"
          + "/roll\n"
          + "/repeat\n"
          + "/horoscope\n"
          + "/bms\n"
          + "_Add \'help\' after a command to get the syntax._")


def get_group_link(command:str):
    """
    Get the group-invite link for the grasmaaier chat
    """
    items = command.split(" ")
    if len(items) == 2:
        if items[1] == "help":
            return ("*Syntax help for /link:*\n"
                  + "just use \'/link\'...\n"
                  + "Out of sheer spite I will make you retype the command\n"
                  + ">:D\n")
    return "https://chat.whatsapp.com/L2xVHEBzWDM0cXWjif8TDf"


def get_horoscope(command:str):
    """
    Functionality:
        Gets the current horoscope.
        
    args:
        command: The given command, should be /horoscope [horoscope sign]

    Returns:
        String with response to client.
    """
    items = command.split(" ")
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
    
    
def get_repeated_command(command):
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


def get_bms_script(command):
    items = command.split(" ")
    if len(items) == 2:
        if items[1] == "help":
            return ("*Syntax help for /bms:*\n"
                  + "Just use '/bms'...\n"
                  + "\n"
                  + "Like, there's nothing else this command could possibly do except send the bee movie script :/")
        
    elif len(items) == 1:
        f = open("./bot/bee_movie_script.txt", 'r')
        script = f.read()
        f.close()
        return script
    
    elif len(items) == 8:
        return "Oh look who has checked the code ;)"
    
    else:
        return "Error in the syntax"