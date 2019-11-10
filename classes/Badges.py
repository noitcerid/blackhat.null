"""
Badges class: Manages badges the hacker can earn throughout the game
"""

BADGES = [[1, "Beginner's Luck", "Make your first hack"],
          2, "Two's a Company", "Make a second attack on the same server/network."]


class Badges:
    id: int
    name: str
    description: str

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
