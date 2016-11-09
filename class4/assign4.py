import re
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
pynet_rtr2_connection.sendline("configure terminal")
pynet_rtr2_connection.expect("\(config\)#")
pynet_rtr2_connection.sendline("logging buffered 9091")
pynet_rtr2_connection.expect("\(config\)#")
pynet_rtr2_connection.sendline("exit")
pynet_rtr2_connection.expect("pynet-rtr2#")

pattern = re.compile(r'^logging.*[0-9]*$', re.MULTILINE)
pynet_rtr2_connection.sendline("show running-config | include logging buffered")
pynet_rtr2_connection.expect(pattern)
print pynet_rtr2_connection.after

