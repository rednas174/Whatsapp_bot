# Whatsapp bot

This is a whatsapp bot made by rednas174 with Flask to serve as a server.  
The IP is not exposed and doesn't need to be port forwarded. It is only reachable within the network itself.


## Requirements

This implementation requires the following:
- A mobile phone with a SIM-card.
- [This app](https://play.google.com/store/apps/details?id=com.pransuinc.autoreply) on the dedicated phone.
- A server that can run Python3 (I use a Raspberry Pi 3B).
- Flask installed on your server.
- [Docker](https://www.docker.com/products/docker-desktop) on your PC.
- [Balena](https://www.balena.io/) if you want to use that.


## Installation

Sign in to Balena and flash the OS to an SD-card.  
Make a new application and flash the OS they give you (It's individually made for each application).

Use balena to push the image. It's automatically build locally and pushes the docker in the folder you are in.

```bash
balena push <application name>
```

If you don't want to use Balena, then copy the .py files to your server.  
If Raspberry Pi is used, use [this](https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d) installation.

*TL;DR of website:*
```bash
sudo apt-get install python3-flask
```

Otherwise, install it using pip.
```bash
pip install flask
```


## Usage

Use the provided app:

- Tap "+".
- Choose "WA Official".
- Set "Received message pattern" to "/".
- Set to "Start with".
- Scroll down and select "Connect to own server".
- Enter "https://your_ip_here:5000".
- Change "Reply to" to "Both".
- Leave the rest as-is.
- Press ✔ and Endure the ad.


## Tips 'n Tricks

Keep the phone on a charger and have both apps open in RAM, but turn the phone into standby mode with whatsapp as open.
I don't know why, but this setup keeps it working. I myself used a Raspberry Pi 3B+ and a Nokia 7 plus.


## Contributing

I aint taking no contributions unless they're actually good... unlike my code :P


## License

I'm not responsable for a whatsapp ban, for a lost phone, for breaking your house's security, for stealing your toes, for flipping your flippos, for removing your dungans, for yinging your yangs, for any damages made, for a nuclear plant made with this code, for the increased probability of you making a logical fallacy, for any Rayquazas that might attack you from the sky, for any jonkos smoked, and for any other possible negative side effect taken or made from this code including a headache from reading it.

[MIT](https://choosealicense.com/licenses/mit/)
