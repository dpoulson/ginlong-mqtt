# Overview
 
This is a daemon that will listen on a port for connections from a Ginlong Solar Inverter. Currently tested with a Solis 4G Mini Single Phase Inverter (Solis-mini-1500-4G)

Many thanks go to Graham0 and his script for an older version. https://github.com/graham0/ginlong-wifi

# Details
The Solis solar inverters come with the option for wired or wireless monitoring 'sticks'. These are designed to talk to their own portal at http://www.ginlongmonitoring.com/ where
the stats will gather. This software allows you to run your own gatherer on a server and push these stats into an MQTT queue for use in other systems such as the OpenHAB home
automation software. 

You will need a system running python with the following modules:
* paho.mqtt.publish
* socket
* binascii
* time
* sys
* string

You will also need a running MQTT server.


 

