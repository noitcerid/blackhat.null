"""
This class contains details around the contents of a server, mostly based on it's type. Will contain one of the following:
- Files - Contain a set of metadata for a file
- Banks Accounts - Contain metadata for account
- Databases - Contains a list of tables/rows
"""


class Contents:
    def __init__(self, contents: list):
        self.data: list = contents

    def add_data(self, data):
        self.data.append(data)

    def remove_data(self, data):
        self.data.remove(data)


class File(Contents):
    def __init__(self, files: list):
        self.files: list = files

    def add_file(self, file):
        self.files.append(file)

    def remove_file(self, file):
        self.files.remove(file)

    # TODO: Need to extend Files class further
    # TODO: Add additional methods for altering file contents


class Bank(Contents):
    def __init__(self, accounts: list):
        self.accounts: list = accounts

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account):
        self.accounts.remove(account)

    # TODO: Add additional functions for altering balances


class Database(Contents):
    def __init__(self, records: list):
        self.records: list = records

    def add_record(self, record):
        self.records.append(record)

    def remove_record(self, record):
        self.records.remove(record)

    def update_record(self, record):
        # TODO: Update method to allow modification of existing record
        pass
