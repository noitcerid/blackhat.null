"""
This class contains details around the contents of a server, mostly based on it's type. Will contain one of the following:
- Files - Contain a set of metadata for a file
- Banks Accounts - Contain metadata for account
- Databases - Contains a list of tables/rows

"""


class Contents:
    def __init__(self, contents: list):
        self._data: list = contents

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    def add_data(self, data):
        self._data.append(data)

    def remove_data(self, data):
        self._data.remove(data)


class File(Contents):
    def __init__(self, files: list):
        self._files: list = files

    @property
    def files(self):
        return self._files

    @files.setter
    def files(self, files):
        self._files = files

    def add_file(self, file):
        self._files.append(file)

    def remove_file(self, file):
        self._files.remove(file)

    # TODO: Need to extend Files class further
    # TODO: Add additional methods for altering file contents


class Bank(Contents):
    def __init__(self, accounts: list):
        self._accounts: list = accounts

    @property
    def accounts(self, accounts):
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        self._accounts = accounts

    def add_account(self, account):
        self._accounts.append(account)

    def remove_account(self, account):
        self._accounts.remove(account)

    # TODO: Add additional functions for altering balances


class Database(Contents):
    def __init__(self, records: list):
        self._records: list = records

    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, records):
        self._records = records

    def add_record(self, record):
        self._records.append(record)

    def remove_record(self, record):
        self._records.remove(record)

    def update_record(self, record):
        # TODO: Update method to allow modification of existing record
        pass
