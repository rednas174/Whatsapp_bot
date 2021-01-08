# Whatsapp bot

This is a whatsapp bot made by hirasloth in Flask to serve as a server.  
The IP is not exposed and doesn't need to be port forwarded. It is only reachable within the network itself.


## Requirements

This implementation requires the following:
- A mobile phone with a SIM-card
- [This app on the dedicated phone](https://play.google.com/store/apps/details?id=com.pransuinc.autoreply)
- A server that can run Python3
- Flask installed.


## Installation

If Raspberry Pi is used, use [this](https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d) installation.

*TL;DR:*
```bash
sudo apt-get install python3-flask
```

## Usage

Use the provided app:

- Tap "+"
- Choose "WA Official"
- Enter the "/roll" pattern under "Received message pattern"
- I personally use "Start with".
- Scroll down and select "Connect to own server".
- Enter "https://your_ip_here:5000"
- Change "Reply to" to "Both"
- Leave the rest as-is.

## Tips 'n Tricks

Keep the phone on a charger and have both apps open in RAM, but turn the phone into standby mode with whatsapp as open.
I don't know why, but this setup keeps it working. I myself used a Raspberry Pi 3B+ and a Nokia 7 plus.


## Contributing

I aint taking no contributions unless they're actually good... unlike my code :P



## License

I'm not responsable for a whatsapp ban, for a lost phone, for breaking your house's security, for stealing your toes, for flipping your flippos, for removing your dungans, for yinging your yangs, for any damages made, for a nuclear plant made with this code, for the increased probability of you making a logical fallacy, for any jonkos smoked, and for any other possible negative side effect taken or made from this code including a headache from reading it.

[MIT](https://choosealicense.com/licenses/mit/)