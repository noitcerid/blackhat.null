"""
Company class
"""

from classes import Employee


class Company:
    def __init__(self, company_id, name, description, size, revenue, formed, employees=None):
        # TODO: Make these private and establish proper get/sets
        self.company_id: int = company_id
        self.name: str = name
        self.description: str = description
        self.size: int = size
        self.revenue: float = revenue
        self.formed: int = formed
        self.employees: list = employees

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    def set_size(self, size):
        self.size = size

    def set_revenue(self, revenue):
        self.revenue = revenue

    def set_formed(self, formed):
        self.formed = formed

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)
