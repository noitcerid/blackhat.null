"""
Testing related to Badge Class
"""

import pytest
from classes.Badge import Badge


class TestBadges:

    @pytest.fixture()
    def supply_sample_badge(self):
        badge = Badge(1, "Test Badge Name", "Test Badge Description")

        return badge

    def test_set_badge_id(self, supply_sample_badge):
        new_id = 0
        supply_sample_badge.badge_id = new_id
        assert supply_sample_badge.badge_id == new_id

    def test_set_name(self, supply_sample_badge):
        new_name = "New Badge Name"
        supply_sample_badge.name = new_name
        assert supply_sample_badge.name == new_name

    def test_set_description(self, supply_sample_badge):
        new_description = "New Badge Description"
        supply_sample_badge.description = new_description
        assert supply_sample_badge.description == new_description

    def test_get_badge_id(self, supply_sample_badge):
        badge_id = 1
        assert supply_sample_badge.badge_id == badge_id

    def test_get_name(self, supply_sample_badge):
        name = "Test Badge Name"
        assert supply_sample_badge.name == name

    def test_get_description(self, supply_sample_badge):
        description = "Test Badge Description"
        assert supply_sample_badge.description == description
