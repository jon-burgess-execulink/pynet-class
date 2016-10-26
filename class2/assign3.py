import telnetlib
import time
import socket
import sys
import getpass

class TelnetConnection(object):

    def __init__(self, ip, username, password, port, timeout):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port
        self.timeout = timeout
        self.connection = ''
    
    def create_connection(self):
        try: 
            connection = telnetlib.Telnet(self.ip, self.port, self.timeout)
            return connection
        except:
            sys.exit("Connection timed-out")

    def login(self):
        output = self.connection.read_until("sername:", self.timeout)
        self.connection.write(self.username + '\n')
        output += self.connection.read_until("ssword:", self.timeout)
        self.connection.write(self.password + '\n')
        return output
    def send_command(self, cmd):
        cmd = cmd.rstrip()
        self.connection.write(cmd + '\n')
        time.sleep(1)
        return self.connection.read_very_eager()
    
    def disable_paging(self, paging_cmd='terminal length 0'):
        return self.send_command(paging_cmd)
    
    def close_connection(self):
        self.connection.close()
        
def main():
    ip_addr = raw_input("IP address: ")
    ip_addr = ip_addr.strip()
    username = 'pyclass'
    password = getpass.getpass()
    telnet_port = 23
    telnet_timeout = 6
    
    my_connection = TelnetConnection(ip_addr, username, password, telnet_port, telnet_timeout)
    my_connection.connection = my_connection.create_connection()
   
    my_connection.login()
    my_connection.disable_paging()
    output = my_connection.send_command('show ip int brief')

    print "\n\n"
    print output
    print "\n\n"
    
    my_connection.close_connection()
    
    
if __name__ == "__main__":
    main()