"""
Menu class for navigation through the terminal
"""


class Menu:
    def __init__(self, name: str, description: str, options: list):
        self.name = name
        self.description = description
        self.options = options

    def __str__(self):
        menu = f"{self.name}\n\n" + \
               f"{self.description}\n\n"

        for i in self.options:
            menu += f"{i[0]}: {i[1]}\n"

        return menu
