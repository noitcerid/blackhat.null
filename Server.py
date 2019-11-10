"""
This is the server class.
"""

from Contents import Contents

SECURITY_LEVELS = [1, 2, 3, 4]


class Server:
    id: int = None
    name: str = None
    type: str = None
    ip_address: str = None
    security_level: int = None
    contents: Contents = None

    def __init__(self, id: int, name: str, type: str, ip_address: str, security_level: int, contents: Contents):
        self.id = id
        self.name = name
        self.type = type
        self.ip_address = ip_address
        self.security_level = security_level
        self.contents = contents

    def get_properties(self):
        return [self.id, self.name, self.type, self.ip_address, self.security_level, self.contents]

    def __str__(self):
        result = "Server ID: " + str(self.id) + \
                 "\nServer Name: " + self.name + \
                 "\nIP Address: " + self.ip_address + \
                 "\nSecurity Level: " + str(self.security_level) + \
                 "\nContents: " + str(self.contents)

        return result
