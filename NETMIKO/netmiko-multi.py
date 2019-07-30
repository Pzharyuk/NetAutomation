import netmiko
import json
import csv                                                                                                

devices = '''
172.16.1.129
172.16.1.130
172.16.1.131
172.16.1.132
'''.strip().splitlines()

device_type = 'cisco_ios'
username = 'cisco'
password = 'cisco'

for device in devices:
    try:
        print('~'*79)
        print('Connecting to devce', device)
        connection = netmiko.ConnectHandler(ip=device, device_type=device_type, 
                                        username=username, password=password)
        output = connection.send_command("show ip arp")
        print(output)
        connection.disconnect()
    except netmiko.ssh_exception.NetMikoAuthenticationException:
        print('authentication failed ', device)

