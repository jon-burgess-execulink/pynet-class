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

pynet1 = ConnectHandler(**pynet1)
pynet2 = ConnectHandler(**pynet2)


pynet1.send_config_from_file(config_file='config.txt')
pynet2.send_config_from_file(config_file='config.txt')
