from netmiko import ConnectHandler


pynet1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': '88newclass',
}

pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': '88newclass',
}

pynet_srx = {
    'device_type': 'juniper',
    'ip': '184.105.247.76',
    'username': 'pyclass',
    'password': '88newclass',
}


pynet1 = ConnectHandler(**pynet1)
pynet2 = ConnectHandler(**pynet2)
pynet_srx = ConnectHandler(**pynet_srx)

output = pynet1.send_command("show arp")
print output

output = pynet2.send_command("show arp")
print output

output = pynet_srx.send_command("show arp")
print output