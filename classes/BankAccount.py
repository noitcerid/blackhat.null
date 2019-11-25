"""
Class specific to bank accounts (inherits from Account class)
"""

from classes import Account


class BankAccount(Account):
    def __init__(self):
        balance: int
        statement: list
