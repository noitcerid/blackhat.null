"""
Testing related to Mission class/interactions
"""

import pytest
from classes.Mission import Mission


class TestMission:

    @pytest.fixture()
    def supply_sample_mission(self):
        mission = Mission("Test Mission", "Welcome to Hacker.Null. This mission will give a safe space to attempt your \
            first hack. Nothing will be traced in the event you do not complete it successfully. Connect to the server\
            listed below and copy the file 'test_file.data' to your memory bank. Disconnect from the server, \
            covering your tracks and then upload the file to the Hacker.Null FTP site. Once uploaded, respond\
            to this message and we will verify you have completed the tutorial correctly. Good luck agent.", 0, 0)

        return mission

    def test_mission_is_completed(self):
        assert 1 == 1

    def test_mission_is_in_progress(self):
        assert 1 == 1
