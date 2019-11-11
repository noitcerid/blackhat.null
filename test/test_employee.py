"""
Testing related to Employee class/interactions
"""

import pytest
from classes.Employee import Employee
from classes.Company import Company


class TestEmployee:

    @pytest.fixture()
    def supply_sample_employee(self):
        employer = Company(1, "Bob's Computer Repair", "Fixing computers since 1992!", 4, 100000, 1992, None)
        employee = Employee(1, "Bob", "Smith", "111-22-3333", "111-222-3333", "123 Anywhere Rd.", "Orlando", "FL",
                            "32830", employer, "Network Engineer", 123200.00, ["Network Security, Class 1"])
        return employee

    def test_set_first_name(self, supply_sample_employee):
        new_first_name = "New Bob"
        supply_sample_employee.first_name = new_first_name
        assert supply_sample_employee.first_name == new_first_name

    def test_set_last_name(self, supply_sample_employee):
        new_last_name = "New Smith"
        supply_sample_employee.last_name = new_last_name
        assert supply_sample_employee.last_name == new_last_name

    def test_set_ssn(self, supply_sample_employee):
        new_ssn = "987-65-4321"
        supply_sample_employee.ssn = new_ssn
        assert supply_sample_employee.ssn == new_ssn

    def test_set_phone(self, supply_sample_employee):
        new_phone = "222-333-4444"
        supply_sample_employee.phone = new_phone
        assert supply_sample_employee.phone == new_phone

    def test_set_address(self, supply_sample_employee):
        new_address = "24123 New Someplace St."
        supply_sample_employee.address = new_address
        assert supply_sample_employee.address == new_address

    def test_set_city(self, supply_sample_employee):
        new_city = "Scottville"
        supply_sample_employee.city = new_city
        assert supply_sample_employee.city == new_city

    def test_set_state(self, supply_sample_employee):
        new_state = "MI"
        supply_sample_employee.state = new_state
        assert supply_sample_employee.state == new_state

    def test_set_postal_code(self, supply_sample_employee):
        new_postal_code = "49454"
        supply_sample_employee.postal_code = new_postal_code
        assert supply_sample_employee.postal_code == new_postal_code

    def test_set_company(self, supply_sample_employee):
        new_company = Company(2, "New Bob's Computer Repair", "Fixing computers since 2008!", 7, 50000, 2008, None)
        supply_sample_employee.employed_by = new_company
        assert supply_sample_employee.employed_by == new_company

    def test_set_position(self, supply_sample_employee):
        new_position = "Lead Network Engineer"
        supply_sample_employee.position = new_position
        assert supply_sample_employee.position == new_position

    def test_set_salary(self, supply_sample_employee):
        new_salary = 120000.00
        supply_sample_employee.salary = new_salary
        assert supply_sample_employee.salary == new_salary

    def test_add_qualification(self, supply_sample_employee):
        new_qualification = "CIS Network Penetration Tester, Class 2"
        supply_sample_employee.add_qualification(new_qualification)
        assert new_qualification in supply_sample_employee.qualifications

    def test_remove_qualification(self, supply_sample_employee):
        old_qualification = "Network Security, Class 1"
        supply_sample_employee.remove_qualification(old_qualification)
        assert old_qualification not in supply_sample_employee.qualifications
