"""
This class contains details around the contents of a server, mostly based on it's type. Will contain one of the following:
- Files - Contain a set of metadata for a file
- Banks Accounts - Contain metadata for account
- Databases - Contains a list of tables/rows

"""


class Contents:
    data: list = None

    def __init__(self, contents: list):
        self.data = contents


class File(Contents):
    files: list

    def __init__(self, files: list):
        self.files = files


class Bank(Contents):
    accounts: list

    def __init__(self, accounts: list):
        self.accounts = accounts


class Database(Contents):
    records: list

    def __init__(self, records: list):
        self.records = records
