"""
This is the server class.
"""

from classes.Contents import Contents

SECURITY_LEVELS = [1, 2, 3, 4]


class Server:
    server_id: int = None
    name: str = None
    server_type: str = None
    ip_address: str = None
    security_level: int = None
    contents: Contents = None

    def __init__(self, server_id, name, server_type, ip_address, security_level, contents: Contents):
        self.id = server_id
        self.name = name
        self.type = server_type
        self.ip_address = ip_address
        self.security_level = security_level
        self.contents = contents

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
