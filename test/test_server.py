"""
Test class for interactions with Servers
"""

import pytest
from classes.Server import Server
from classes.Contents import Contents


class TestFileServer:

    @pytest.fixture()
    def supply_sample_file_servers(self):
        contents1 = Contents([["file1.dat", "Some text data", 12],
                              ["file2.dat", "Some text data", 5],
                              ["file3.dat", "Some text data", 3]])
        contents2 = Contents([["file1.dat", "Some text data", 12],
                              ["file5.dat", "Some text data", 5],
                              ["file6.dat", "Some text data", 3]])
        server_list = [Server(1, "Test Server 1", "File", "1.1.1.1", 1, contents1),
                       Server(2, "Test Server 2", "File", "2.2.2.2", 1, contents2)]

        return server_list

    def test_file_exists(self, supply_sample_file_servers):
        contents1 = supply_sample_file_servers[0].contents.data
        contents2 = supply_sample_file_servers[1].contents.data

        file_to_find = ["file1.dat", "Some text data", 12]
        assert file_to_find in contents1
        assert file_to_find in contents2

    def test_file_update(self, supply_sample_file_servers):
        server = supply_sample_file_servers[0]
        contents = server.contents.data
        file_to_update = contents[0]
        new_file_data = ["file1.dat", "Some different text data", 13]
        server.contents.update_data(file_to_update, new_file_data)

        assert new_file_data in server.contents.data


class TestBankServer:
    @pytest.fixture()
    def supply_sample_bank_servers(self):
        accounts1 = Contents([[1234, "AccountOwner1", 100],
                              [2345, "AccountOwner2", 10]])
        accounts2 = Contents([[3456, "AccountOwner3", 1000],
                              [4567, "AccountOwner4", 10000]])

        server_list = [Server(1, "Bank 1", "Bank", "1.1.1.1", 2, accounts1),
                       Server(2, "Bank 2", "Bank", "2.2.2.2", 2, accounts2)]

        return server_list

    def test_account_exists(self, supply_sample_bank_servers):
        accounts1 = supply_sample_bank_servers[0].contents.data
        accounts2 = supply_sample_bank_servers[1].contents.data

        account_to_find = [1234, "AccountOwner1", 100]
        for account in accounts1:
            if account_to_find[0] == account[0]:
                assert account_to_find[0] == account[0]

    def test_account_balance_update(self, supply_sample_bank_servers):
        pass
