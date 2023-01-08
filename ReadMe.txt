Email-IP 1.1.0 - Email automatically your public IP.
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
along with this program.  If not, see <https://www.gnu.org/licenses/>.

-----------------------------------------------------------------------------------------------
Description:
The program can check a computer public Internet IP and email it. You can use it
to email yourself, on another system or on your phone, the public Internet IP of a computer you are using as a web or FTP server, for remote desktop, or any other use for remote access to your system.

Instructions:
- Unzip the package to a folder.
- Open the config.txt file and edit as specified (be accurate or the program
   will crash).
- In the config file you must specify sender and receiver address, smtp server,
   SMTP username and password, SMTP port.
- Do not delete the config.txt file or the program will crash
- Run the program (Email-IP.exe).
- The program will email your IP to the address specified in the config.txt file.
- The checkip.dyndns.com server will be polled every minute. If the IP changes,
   the program will email the new IP again to the specified address.
- Create a shortcut of the program and copy it into the startup folder to start the
   program automatically.
- The program has no GUI (for now). The IP and messages of successfully sent 
   email or no connection will be displayed in a command promt window.
- The program will also generate two files: IP.txt (containing the IP) and
   timestamp.txt (a log of connections/disconnections + IP).
- If you specify a local or remote folder in the config.txt file, by replacing the "path"
  parameter with your path, the program will copy the IP.txt and timestamp.txt
  files to the specified path. This is useful if you want to check your IP and the
  connection log by accessing from remote a cloud or FTP server folder stored on        your computer.
- Press "q" repeatedly to quit the program.