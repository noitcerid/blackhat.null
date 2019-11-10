"""
Hacker class
"""


class Hacker:
    name: str
    alias: str
    password: str
    rank: int
    rating: int
    badges: list = None

    def __init__(self, name, alias, password, rank, rating):
        self.name = name
        self.alias = alias
        self.password = password
        self.rank = rank
        self.rating = rating

    def get_name(self):
        return self.name

    def get_alias(self):
        return self.alias

    def get_password(self):
        return self.password

    def get_rank(self):
        return self.rank

    def get_rating(self):
        return self.rating

    def get_badges(self):
        return self.badges

    def set_name(self, name):
        self.name = name

    def set_alias(self, alias):
        self.alias = alias

    def set_password(self, password):
        self.password = password

    def set_rank(self, rank):
        self.rank = rank

    def set_rating(self, rating):
        self.rating = rating

    def add_badge(self, badge):
        self.badges.append(badge)
