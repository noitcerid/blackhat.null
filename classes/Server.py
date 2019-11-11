"""
This is the server class.
"""

from classes.Contents import Contents

SECURITY_LEVELS = [1, 2, 3, 4]


class Server:
    def __init__(self, server_id, name, server_type, ip_address, security_level, contents: Contents):
        self.id: int = server_id
        self.name: str = name
        self.type: str = server_type
        self.ip_address: str = ip_address
        self.security_level: int = security_level
        self.contents: Contents = contents

    def get_properties(self):
        return [self.server_id, self.name, self.server_type, self.ip_address, self.security_level, self.contents]

    def __str__(self):
        result = "Server ID: " + str(self.server_id) + \
                 "\nServer Name: " + self.name + \
                 "\nServer Type: " + self.server_type + \
                 "\nIP Address: " + self.ip_address + \
                 "\nSecurity Level: " + str(self.security_level) + \
                 "\nContents: " + str(self.contents)

        return result
