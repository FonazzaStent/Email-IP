"""Email-IP 1.0.0 - Email automatically your public IP.
Copyright (C) 2022  Fonazza-Stent

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


def getIP():
    try:
        d = str(urlopen('http://checkip.dyndns.com/').read())
        return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)
    except:
        return('127.0.0.1')

parameters=[]

configfile=open("config.txt",'r')
for n in range (0,6):
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
#print (parameters)
 
while True:
    print(getIP())
    IPnum=str(getIP())
    IPfile=open("IP.txt",'r')
    oldIP=IPfile.read()
    IPfile.close()

    if IPnum != oldIP:
        message = """From: From """+sender+""" To: """+receiver+"""
        Subject: IP Address

        """ +IPnum
        try:
            smtpObj = smtplib.SMTP(SMTPserver,port)
            smtpObj.login(username,password)
            smtpObj.sendmail(sender, receiver, message)
            print("Successfully sent email")
        except:
            print("no connection")

        IPfile=open("IP.txt",'w')
        IPfile.write(IPnum)
        IPfile.close()
    for n in range (1,60):
        if keyboard.is_pressed("q"):
            quit()
        time.sleep(1)
        #print ("-",end="")

