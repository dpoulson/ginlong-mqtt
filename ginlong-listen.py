#!/usr/bin/python

import paho.mqtt.publish as publish
import socket
import binascii
import time
import sys
import string

###########################
# Variables

listen_address = "0.0.0.0"     # What address to listen to (0.0.0.0 means it will listen on all addresses)
listen_port = 9999             # Port to listen on
client_id = "ginlong"          # MQTT Client ID
mqtt_server = "localhost"      # MQTT Address
mqtt_port = 1833               # MQTT Port

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((listen_address, listen_port))
sock.listen(1)

while True: 
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    conn,addr = sock.accept()
    try:
        print >>sys.stderr, 'connection from', addr
        while True:
            rawdata = conn.recv(1000)                                 # Read in a chunk of data
            print >>sys.stderr, 'received data', rawdata
            hexdata = binascii.hexlify(rawdata)                       # Convert to hex for easier processing
            print >>sys.stderr, 'Hex data: ', hexdata

            if(len(hexdata) != 270):
                msgs = []
                serial = binascii.unhexlify(str(hexdata[42:62]))      # Serial number is used for MQTT path, allowing multiple inverters to connect to a single instance
                print "Serial %s" % serial
                mqtt_topic = ''.join([client_id, "/", serial, "/"])   # Create the topic base using the client_id and serial number

                ##### Vpv1
                vpv1 = float(int(hexdata[66:69],16)/10)
                msgs.append((mqtt_topic + "Vpv1", vpv1, 0, False))

                ##### Vpv2
                vpv2 = float(int(hexdata[70:73],16)/10)
                msgs.append((mqtt_topic + "Vpv2", vpv2, 0, False))

                ##### Ipv1
                ipv1 = float(int(hexdata[78:81],16)/10)
                msgs.append((mqtt_topic + "Ipv1", ipv1, 0, False))

                ##### Ipv2
                ipv2 = float(int(hexdata[82:85],16)/10)
                msgs.append((mqtt_topic + "Ipv2", ipv2, 0, False))

                ##### Vac1
                vac1 = float(int(hexdata[102:105],16)/10)
                msgs.append((mqtt_topic + "Vac1", vac1, 0, False))

                ##### Vac2
                vac2 = float(int(hexdata[106:109],16)/10)
                msgs.append((mqtt_topic + "Vac2", vac2, 0, False))

                ##### Vac3
                vac3 = float(int(hexdata[110:113],16)/10)
                msgs.append((mqtt_topic + "Vac3", vac3, 0, False))

                ##### Iac1
                iac1 = float(int(hexdata[90:93],16)/10)
                msgs.append((mqtt_topic + "Iac1", iac1, 0, False))

                ##### Iac2
                iac2 = float(int(hexdata[94:97],16)/10)
                msgs.append((mqtt_topic + "Iac2", iac2, 0, False))

                ##### Iac3
                iac3 = float(int(hexdata[98:101],16)/10)
                msgs.append((mqtt_topic + "Iac3", iac3, 0, False))

                ##### Pac
                pac = float(int(hexdata[118:121],16)/10)
                msgs.append((mqtt_topic + "Pac", pac, 0, False))

                ##### Fac
                fac = float(int(hexdata[114:117],16)/10)
                msgs.append((mqtt_topic + "Fac", fac, 0, False))

                ##### Temp
                temp = float(int(hexdata[62:65],16)/10)
                msgs.append((mqtt_topic + "Temp", temp, 0, False))

                ##### kWh today
                kwhtoday = float(int(hexdata[138:141],16)/10)
                msgs.append((mqtt_topic + "kwhtoday", kwhtoday, 0, False))

                ##### kWh total
                #kwhtotal = float(int(hexdata[70:73],16)/10)
                #msgs.append((mqtt_topic + "kwhtotal", kwhtotal, 0, False))

                publish.multiple(msgs, hostname="localhost")

    finally:
        conn.close()

