import pexpect
import sys

pynet_rtr2_ip_addr =  "184.105.247.71"
pynet_rtr2_username = 'pyclass'
pynet_rtr2_password = '88newclass'

pynet_rtr2_connection = pexpect.spawn('ssh -l {} {}'.format(pynet_rtr2_username, pynet_rtr2_ip_addr))
#pynet_rtr2_connection.logfile = sys.stdout
pynet_rtr2_connection.timeout = 10
pynet_rtr2_connection.expect('ssword:')
pynet_rtr2_connection.sendline(pynet_rtr2_password)
pynet_rtr2_connection.expect("pynet-rtr2#")
pynet_rtr2_connection.sendline("show ip interface brief")
pynet_rtr2_connection.expect("pynet-rtr2#")
print pynet_rtr2_connection.before

