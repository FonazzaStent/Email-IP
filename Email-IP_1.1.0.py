"""Email-IP 1.1.0 - Email automatically your public IP.
Copyright (C) 2023  Fonazza-Stent

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

from urllib.request import urlopen
import re as r
import smtplib
import os
import shutil
import time
import keyboard

if not os.path.exists("IP.txt"):
    IPfile=open("IP.txt",'w')
    IPfile.close()
if not os.path.exists("timestamp.txt"):
    timefile=open("timestamp.txt",'w')
    timefile.close()


def getIP():
    global timestamp
    timestamp=time.strftime("%d/%m/%Y %H:%M:%S")
    try:
        d = str(urlopen('http://checkip.dyndns.com/').read())
        return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)
    except:
        timefile=open("timestamp.txt",'a')
        timefile.write("Offline: "+timestamp+"\n")
        timefile.close ()
        if os.path.exists(cloud):
            shutil.copyfile("timestamp.txt",cloud+"timestamp.txt")
        else:
            print ("Could not copy timestamp file. Path not valid.")
        return('127.0.0.1')

parameters=[]

configfile=open("config.txt",'r')
for n in range (0,7):
    parameter=configfile.readline()
    parameter=parameter[-2::-1]
    parameter=parameter[::-1]
    parameters.append(parameter)

sender=parameters[0]
receiver=parameters[1]
SMTPserver=parameters[2]
username=parameters[3]
password=parameters[4]
port=parameters[5]
cloud=parameters[6]

while True:
    global timestamp
    print(getIP())
    IPnum=str(getIP())
    IPfile=open("IP.txt",'r')
    oldIP=IPfile.read()
    IPfile.close()


    if IPnum != oldIP and IPnum != "127.0.0.1":
        IPfile=open("IP.txt",'w')
        IPfile.write(IPnum)
        IPfile.close()
        print (timestamp)
        timefile=open("timestamp.txt",'a')
        timefile.write("Online: "+timestamp+" IP: "+IPnum +"\n")
        timefile.close ()
        if os.path.exists(cloud):
            shutil.copyfile("timestamp.txt",cloud+"timestamp.txt")

        sender2="<"+sender+">"
        receiver2="<"+receiver+">"
        subject="IP address"
        text=IPnum+"\n"+timestamp
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (sender, "".join(receiver), subject, text)
        try:
            smtpObj = smtplib.SMTP(SMTPserver,port)
            smtpObj.login(username,password)
            smtpObj.sendmail(sender, receiver, message)
            print("Successfully sent email")
            if os.path.exists(cloud):
                shutil.copyfile("IP.txt",cloud+"IP.txt")

        except:
            print("no connection")
            if os.path.exists(cloud):
                shutil.copyfile("IP.txt",cloud+"IP.txt")

    for n in range (1,120):
        if keyboard.is_pressed("q"):
            quit()
        time.sleep(0.5)


