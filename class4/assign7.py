from netmiko import ConnectHandler

pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': '88newclass',
}

pynet2 = ConnectHandler(**pynet2)

pynet2.config_mode()

if pynet2.check_config_mode():
    pynet2.send_command("logging buffered 22223")
    pynet2.exit_config_mode()
    
else:
    print "error, not in config mode"
