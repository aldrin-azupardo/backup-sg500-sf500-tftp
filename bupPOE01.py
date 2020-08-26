#!/usr/bin/env python
import sys
from time import sleep
import paramiko
import os
import datetime
switch="192.168.X.X"
  
# Create an ssh connection 
conn = paramiko.SSHClient()
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn.connect(switch, username="cisco", password="cisco")
switch_conn = conn.invoke_shell()
print('Successfully connected to %s' % switch)
# Send the command and wait for it to execute
switch_conn.send("copy running-config tftp://192.168.2.33/BACKUP/config.txt exclude\n")
sleep(10)
# Save running-config.txt will be renamed
current_date = datetime.datetime.today().strftime ('%b-%d-%Y')
os.rename(r'/tftpboot/BACKUP/config.txt',r'/tftpboot/BACKUP/POE' + str(current_date) + '.cfg')
print('Backup completed for %s' % switch)
conn.close

