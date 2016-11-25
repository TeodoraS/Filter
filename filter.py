#!/usr/bin/python
import re
import paramiko
import cmd
import untangle
import os
def ssh_connection():
    host = []
#    host.append(raw_input('Insert server host:\t'))
    host.append(raw_input ('Insert username:\t'))
    host.append(raw_input ('Insert password:\t'))

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('172.17.18.150',
                   username = host[0],
                   password = host[1])
    stdin, stdout, stderr = client.exec_command('ls /data/samba/share/')
    print 'Ssh succesfull.'
    stdout = stdout.readlines()
    client.close()
    print stdout

  
#ssh_connection()

#parsing paths
dictionary = []
inputf = open('E:/Python/filter/foss.xml')
obj = inputf.readlines()
pat = re.compile(r'(?:src=).*$')
searchobj = filter(pat.search, obj)

print searchobj
for elem in searchobj:
    print elem
