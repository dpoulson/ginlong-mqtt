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
        #print >>sys.stderr, 'connection from', addr
        # while True:
            rawdata = conn.recv(1000)                                 # Read in a chunk of data
            hexdata = binascii.hexlify(rawdata)                       # Convert to hex for easier processing

            if(len(hexdata) == 270):
                timestamp = (time.strftime("%F %H:%M"))		# get date time
                print >>sys.stderr, 'Hex data: ', hexdata
                msgs = []
                serial = binascii.unhexlify(str(hexdata[70:102]))     # Serial number is used for MQTT path, allowing multiple inverters to connect to a single instance
                print "Serial %s" % serial
                print "Length %s" % len(hexdata)
                mqtt_topic = ''.join([client_id, "/", serial, "/"])   # Create the topic base using the client_id and serial number
                if __debug__:
                    print >>sys.stderr, 'MQTT Topic: ', mqtt_topic

                ##### Vpv1
                vpv1 = float(int(hexdata[108:112],16))/10
                if __debug__:
                    print >>sys.stderr, 'vpv1: ', vpv1
                msgs.append((mqtt_topic + "Vpv1", vpv1, 0, False))

                ##### Vpv2
                #vpv2 = float(int(hexdata[108:112],16))/10
                #if __debug__:
                #    print >>sys.stderr, 'vpv2: ', vpv2
                #msgs.append((mqtt_topic + "Vpv2", vpv2, 0, False))

                ##### Ipv1
                ipv1 = float(int(hexdata[112:116],16))/10
                if __debug__:
                    print >>sys.stderr, 'ipv1: ', ipv1
                msgs.append((mqtt_topic + "Ipv1", ipv1, 0, False))

                ##### Ipv2
                #ipv2 = float(int(hexdata[116:120],16))/10
                #if __debug__:
                #    print >>sys.stderr, 'ipv2: ', ipv2
                #msgs.append((mqtt_topic + "Ipv2", ipv2, 0, False))

                ##### Vac1
                vac1 = float(int(hexdata[144:148],16))/10
                if __debug__:
                    print >>sys.stderr, 'vac1: ', vac1
                msgs.append((mqtt_topic + "Vac1", vac1, 0, False))

                ##### Vac2
                #vac2 = float(int(hexdata[106:109],16))/10
                #if __debug__:
                #    print >>sys.stderr, 'vac2: ', vac2
                #msgs.append((mqtt_topic + "Vac2", vac2, 0, False))

                ##### Vac3
                #vac3 = float(int(hexdata[110:113],16))/10
                #if __debug__:
                #    print >>sys.stderr, 'vac3: ', vac3
                #msgs.append((mqtt_topic + "Vac3", vac3, 0, False))

                ##### Iac1
                iac1 = float(int(hexdata[120:124],16))/10
                if __debug__:
                    print >>sys.stderr, 'iac1: ', iac1
                msgs.append((mqtt_topic + "Iac1", iac1, 0, False))

                ##### Iac2
                #iac2 = float(int(hexdata[124:128],16))/10
                #if __debug__:
                #    print >>sys.stderr, 'iac2: ', iac2
                #msgs.append((mqtt_topic + "Iac2", iac2, 0, False))

                ##### Iac3
                #iac3 = float(int(hexdata[128:132],16))/10
                #if __debug__:
                #    print >>sys.stderr, 'iac3: ', iac3
                #msgs.append((mqtt_topic + "Iac3", iac3, 0, False))

                ##### Pac
                pac = float(int(hexdata[140:144],16))/10
                if __debug__:
                    print >>sys.stderr, 'pac: ', pac
                msgs.append((mqtt_topic + "Pac", pac, 0, False))

                ##### Fac
                fac = float(int(hexdata[148:152],16))/100
                if __debug__:
                    print >>sys.stderr, 'fac: ', fac
                msgs.append((mqtt_topic + "Fac", fac, 0, False))

                ##### Temp
                temp = float(int(hexdata[102:104],16))/10
                if __debug__:
                    print >>sys.stderr, 'temp: ', temp
                msgs.append((mqtt_topic + "Temp", temp, 0, False))

                ##### kWh today
                kwhtoday = float(int(hexdata[156:160],16))/100
                if __debug__:
                    print >>sys.stderr, 'kwhtoday: ', kwhtoday
                msgs.append((mqtt_topic + "kwhtoday", kwhtoday, 0, False))

                ##### kWh total
                kwhtotal = float(int(hexdata[164:168],16))/10
                if __debug__:
                    print >>sys.stderr, 'kwhtotal: ', kwhtotal
                msgs.append((mqtt_topic + "kwhtotal", kwhtotal, 0, False))

                #publish.multiple(msgs, hostname="localhost")
                file = open("rawlog",'a')
                file.write(timestamp + ' ' + hexdata + '\n')
                file.close()

    finally:
        print "Finally"
