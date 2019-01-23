#Connecting to the device via SSH
session = ConnectHandler(device_type = device_type, ip = ip, username = username, password = password, global_delay_factor = 3)
 
#Entering enable mode
enable = session.enable()
 
#Sending the command and storing the output (running configuration)
output = session.send_command(command)
