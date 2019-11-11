"""
Badge class: Manages badges the hacker can earn throughout the game
"""

BADGES = [[1, "Beginner's Luck", "Make your first hack"],
          2, "Two's a Company", "Make a second attack on the same server/network."]


class Badge:
    def __init__(self, badge_id, name, description):
        # TODO: Make private and establish proper get/sets
        self.badge_id: int = badge_id
        self.name: str = name
        self.description: str = description
