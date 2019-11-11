"""
Hacker class
"""


class Hacker:
    def __init__(self, name, alias, password, rank, rating, badges):
        self._name = name
        self._alias = alias
        self._password = password
        self._rank = rank
        self._rating = rating
        self._badges = badges

    @property
    def name(self):
        return self._name

    @property
    def alias(self):
        return self._alias

    @property
    def password(self):
        return self._password

    @property
    def rank(self):
        return self._rank

    @property
    def rating(self):
        return self._rating

    @property
    def badges(self):
        return self._badges

    @name.setter
    def name(self, name):
        self._name = name

    @alias.setter
    def alias(self, alias):
        self._alias = alias

    @password.setter
    def password(self, password):
        self._password = password

    @rank.setter
    def rank(self, rank):
        self._rank = rank

    @rating.setter
    def rating(self, rating):
        self._rating = rating

    def add_badge(self, badge):
        self._badges.append(badge)
