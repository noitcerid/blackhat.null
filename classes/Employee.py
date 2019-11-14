"""
Employee class
"""

from classes.Qualification import Qualification


class Employee:
    def __init__(self, employee_id, first_name, last_name, ssn, phone, address, city,
                 state, postal_code, employed_by, position, salary,
                 qualifications):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.employed_by = employed_by
        self.position = position
        self.salary = salary
        self.qualifications = qualifications

    def add_qualification(self, qualification):
        self.qualifications.append(qualification)

    def remove_qualification(self, qualification):
        self.qualifications.remove(qualification)
