"""
This is the server class.
"""

from classes.Contents import Contents

SECURITY_LEVELS = [1, 2, 3, 4, 5, 6, 7]


class Server:
    def __init__(self, server_id, name, server_type, ip_address, security_level, contents: Contents):
        self.id: int = server_id
        self.name: str = name
        self.type: str = server_type
        self.ip_address: str = ip_address
        self.security_level: int = security_level
        self.contents: Contents = contents

    def get_properties(self):
        return [self.id, self.name, self.type, self.ip_address, self.security_level, self.contents]

    def search_contents(self, search_string):
        if search_string in self.contents:
            return self.contents

    def __str__(self):
        return (
                f"Server ID: {self.id}\n"
                f"Server Name: {self.name}\n"
                f"Server Type: {self.type}\n"
                f"IP Address: {self.ip_address}\n"
                f"Security Level: {self.security_level}\n"
                f"Contents: {self.contents}"
        )
