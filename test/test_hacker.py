"""
Testing related to Hacker class/interactions
"""

import pytest
from classes.Hacker import Hacker
from classes.Badge import Badge


class TestHacker:

    @pytest.fixture()
    def supply_sample_hacker(self):
        hacker = Hacker("Hacker Name", "AnAlias", "password", 1, 1,
                        Badge(1, "Getting Started", "Make your first hack!"))
        return hacker

    def test_set_name(self, supply_sample_hacker):
        new_name = "New Hacker Name"
        supply_sample_hacker.name = new_name
        assert supply_sample_hacker.name == new_name

    def test_set_alias(self, supply_sample_hacker):
        new_alias = "NewHackerAlias"
        supply_sample_hacker.alias = new_alias
        assert supply_sample_hacker.alias == new_alias

    def test_set_password(self, supply_sample_hacker):
        new_password = "newpassword"
        supply_sample_hacker.password = new_password
        assert supply_sample_hacker.password == new_password

    def test_set_rank(self, supply_sample_hacker):
        new_rank = 2
        supply_sample_hacker.rank = new_rank
        assert supply_sample_hacker.rank == new_rank

    def test_set_rating(self, supply_sample_hacker):
        new_rating = 2
        supply_sample_hacker.rating = new_rating
        assert supply_sample_hacker.rating == new_rating

    def test_get_name(self, supply_sample_hacker):
        name = "Hacker Name"
        assert supply_sample_hacker.name == name

    def test_get_alias(self, supply_sample_hacker):
        alias = "AnAlias"
        assert supply_sample_hacker.alias == alias

    def test_get_password(self, supply_sample_hacker):
        password = "password"
        assert supply_sample_hacker.password == password

    def test_get_rank(self, supply_sample_hacker):
        rank = 1
        assert supply_sample_hacker.rank == rank

    def test_get_rating(self, supply_sample_hacker):
        rating = 1
        assert supply_sample_hacker.rating == rating

    def test_get_badges(self, supply_sample_hacker):
        badge = Badge(1, "Getting Started", "Make your first hack!")
        return supply_sample_hacker.badges == badge
