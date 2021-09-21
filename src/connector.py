import netmiko
from netmiko import ConnectHandler

class Connector:

    def Connect( self, device_type = "linux",address = "127.0.0.1", username = "root", password = "root", port = 22, command = "whoami" ):

        try:
        
            listConnect = {

                "device_type"  : device_type,
                "ip"           : address,
                "username"     : username,
                "password"     : password,
                "port"         : str(port),
                "secret"       : password
            }

            connect = ConnectHandler( **listConnect )
            connect.enable()
            connect.send_command( command )

            return True

        except netmiko.ssh_exception.NetmikoTimeoutException:

            return "Common causes of this problem are:\n1. Incorrect hostname or IP address.\n2. Wrong TCP port.\n3. Intermediate firewall blocking access."