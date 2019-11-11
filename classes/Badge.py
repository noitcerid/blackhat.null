"""
Badge class: Manages badges the hacker can earn throughout the game
"""

BADGES = [[1, "Beginner's Luck", "Make your first hack"],
          2, "Two's a Company", "Make a second attack on the same server/network."]


class Badge:
    badge_id: int
    name: str
    description: str

    def __init__(self, badge_id, name, description):
        self.badge_id = badge_id
        self.name = name
        self.description = description
