"""
Company class
"""

from classes import Employee


class Company:
    id: int
    name: str
    description: str
    size: int
    revenue: float
    formed: int
    employees: list

    def __init__(self, id, name, description, size, revenue, formed, employees=None):
        self.id = id
        self.name = name
        self.description = description
        self.size = size
        self.revenue = revenue
        self.formed = formed
        self.employees = employees

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
