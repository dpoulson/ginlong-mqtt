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


# Setup

1. Log into the monitoring device, and configure the second IP option to point to the server that this daemon is running on. (Daemon defaults to port 9999)
2. Make sure that the MQTT settings are correct in the daemon.
3. Start the daemon
4. Add the following to your OpenHAB items (Replace XXXXXXXXXX with the serial number of your inverter)
```
// Environmentals
Number Solis_Temp "Temperature [%.2f °C]" (Solis) { mqtt="<[mymosquitto:ginlong/XXXXXXXXXX/temp:state:default" }

// DC
Number Solis_DC1Volt "DC Volts [%.2f V]" (Solis) { mqtt="<[mymosquitto:ginlong/XXXXXXXXXX/temp:state:default" }
Number Solis_DC1Amp "DC Current [%.2f A]" (Solis) { mqtt="<[mymosquitto:ginlong/XXXXXXXXXX/temp:state:default" }

// AC
Number Solis_AC1Volt "AC Volts [%.2f V]" (Solis) { mqtt="<[mymosquitto:ginlong/XXXXXXXXXX/temp:state:default" }
Number Solis_AC1Amp "AC Current [%.2f A]" (Solis) { mqtt="<[mymosquitto:ginlong/XXXXXXXXXX/temp:state:default" }

// Stats
Number Solis_kWhToday "kWh today [%.2f kWh]" (Solis) { mqtt="<[mymosquitto:ginlong/XXXXXXXXXX/temp:state:default" }
Number Solis_kWhTotal "kWh total [%.2f kWh]" (Solis) { mqtt="<[mymosquitto:ginlong/XXXXXXXXXX/temp:state:default" }
```
5. These items should now be accessible in your rules. If you have influxdb and grafana set up, you should also be able to start producing graphs




