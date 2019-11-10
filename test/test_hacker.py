"""
Testing related to Hacker class/interactions
"""

import pytest
from classes.Hacker import Hacker


@pytest.fixture()
def supply_sample_hacker():
    hacker = Hacker("Hacker Name", "M0rPh3u5", "password", 1, 1)
    return hacker


def test_hacker_set_name(supply_sample_hacker):
    new_name = "New Hacker Name"
    supply_sample_hacker.set_name(new_name)
    assert supply_sample_hacker.name == new_name


def test_hacker_set_alias(supply_sample_hacker):
    new_name = "NewHackerAlias"
    supply_sample_hacker.set_name(new_name)
    assert supply_sample_hacker.name == new_name


def test_hacker_set_password(supply_sample_hacker):
    new_password = "newpassword"
    supply_sample_hacker.set_password(new_password)
    assert supply_sample_hacker.password == new_password


def test_hacker_set_rank(supply_sample_hacker):
    new_rank = 2
    supply_sample_hacker.set_rank(new_rank)
    assert supply_sample_hacker.rank == new_rank


def test_hacker_set_rating(supply_sample_hacker):
    new_rating = 2
    supply_sample_hacker.set_rating(new_rating)
    assert supply_sample_hacker.rating == new_rating
