import paramiko
import cmd

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
    
ssh_connection()

