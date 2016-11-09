import paramiko
import time

pynet_rtr2_ip_addr =  "184.105.247.71"
pynet_rtr2_username = 'pyclass'
pynet_rtr2_password = '88newclass'

pynet_rtr2_connection_pre = paramiko.SSHClient()
pynet_rtr2_connection_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
pynet_rtr2_connection_pre.connect(pynet_rtr2_ip_addr, username = pynet_rtr2_username, password = pynet_rtr2_password, look_for_keys=False, allow_agent=False)
pynet_rtr2_connection = pynet_rtr2_connection_pre.invoke_shell()

pynet_rtr2_connection.send("terminal length 0\n")
time.sleep(1)
output = pynet_rtr2_connection.recv(65535)
print output
pynet_rtr2_connection.send("conf t\n")
time.sleep(2)
output = pynet_rtr2_connection.recv(65535)
print output
pynet_rtr2_connection.send("logging buffered 10000\n")
pynet_rtr2_connection.send("exit\n")
pynet_rtr2_connection.send("show running-config | inc logging\n")
time.sleep(2)
output = pynet_rtr2_connection.recv(65535)
print output