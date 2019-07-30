from netmiko import ConnectHandler                                                                                                   

host = input(" Enter Device Name: ")
#password = input(" what is your password? ")
device = { 
    'device_type': 'cisco_ios',
    'host': host,
    'username': 'cisco',
    'password': 'cisco',
} 

net_connect = ConnectHandler(**device) 

net_connect.find_prompt()

output = net_connect.send_command("show mac address-table")

#config_commands = ['no vlan 888']

#utput = net_connect.send_config_set(config_commands)

print(output)