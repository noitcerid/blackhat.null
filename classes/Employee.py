"""
Employee class
"""

from classes.Qualification import Qualification


class Employee:
    def __init__(self, employee_id, first_name, last_name, ssn, phone, address, city,
                 state, postal_code, employed_by, position, salary,
                 qualifications):
        self.employee_id: int = employee_id
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.ssn: str = ssn
        self.phone: str = phone
        self.address: str = address
        self.city: str = city
        self.state: str = state
        self.postal_code: str = postal_code
        self.employed_by: str = employed_by
        self.position: str = position
        self.salary: int = salary
        self.qualifications: [Qualification] = qualifications

    def add_qualification(self, qualification):
        self.qualifications.append(qualification)

    def remove_qualification(self, qualification):
        self.qualifications.remove(qualification)

    def __str__(self):
        return (
                f"Details for {self.first_name} {self.last_name} ({self.employee_id}):\n"
                f"\tSocial Security Number: {self.ssn}\n"
                f"\tPhone Number: {self.phone}\n"
                f"\tAddress: {self.address} {self.city}, {self.state} {self.postal_code}\n"
                f"\tEmployer: {self.employed_by}\n"
                f"\tPosition: {self.position}\n"
                f"\tSalary: {self.salary}\n" 
                f"\tQualifications: {self.qualifications}"
        )
