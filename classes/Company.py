"""
Company class
"""

from classes.Employee import Employee


class Company:
    def __init__(self, company_id, name, description, size, revenue, formed, employees=None):
        self.company_id: int = company_id
        self.name: str = name
        self.description: str = description
        self.size: int = size
        self.revenue: float = revenue
        self.formed: int = formed
        self.employees: [Employee] = employees

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def __str__(self):
        return (
            f"Details for {self.name} ({self.company_id}):\n"
            f"\tDescription: {self.description}\n"
            f"\tSize: {self.size}\n"
            f"\tRevenue: {self.revenue}\n"
            f"\tFormed: {self.formed}"
        )
