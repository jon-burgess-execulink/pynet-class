import telnetlib
import time
import socket
import sys

def create_telnet_connection(ip_addr,telnet_port, telnet_timeout):
    try:
        return telnetlib.Telnet(ip_addr, telnet_port, telnet_timeout)
    except socket.timeout:
        return ''

def close_connection(remote_conn):
    if (remote_conn):
        remote_conn.close()
    else:
        return "Connection does not exist"

def send_command(remote_conn, command):
    if (remote_conn):
        command = command.rstrip()
        remote_conn.write(command + '\n')
        time.sleep(1)
        return remote_conn.read_very_eager()

def telnet_login(remote_conn, username, password, user_prompt, pass_prompt):
    output = remote_conn.read_until(user_prompt)
    remote_conn.write(username + '\n')
    output += remote_conn.read_until(pass_prompt)
    remote_conn.write(password + '\n')
    output += remote_conn.read_very_eager()
    return output
    
def main():
    telnet_port = 23
    telnet_timeout = 6

    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'
    
    my_connection = create_telnet_connection(ip_addr,telnet_port, telnet_timeout)
    if(my_connection):
        login = telnet_login(my_connection, username, password, "sername:", "assword:")
        print login
        int_brief = send_command(my_connection,"show ip interface brief")
        print type(int_brief)
        print int_brief
    else:
        sys.exit("A connection error occurred") 
        
    
    
    close_connection(my_connection)
main()