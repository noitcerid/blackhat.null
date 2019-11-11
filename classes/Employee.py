"""
Employee class
"""

from classes import Company


class Employee:
    def __init__(self, employee_id: int, first_name: str, last_name: str, ssn: str, phone: str, address: str, city: str,
                 state: str, postal_code: str, employed_by: Company, position: str, salary: float,
                 qualifications: list):
        self._employee_id: int = employee_id
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn
        self._phone = phone
        self._address = address
        self._city = city
        self._state = state
        self._postal_code = postal_code
        self._employed_by = employed_by
        self._position = position
        self._salary = salary
        self._qualifications = qualifications  # TODO: Make this a strongly typed class for Qualifications

    @property
    def employee_id(self):
        return self._employee_id

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def ssn(self):
        return self._ssn

    @property
    def phone(self):
        return self._phone

    @property
    def address(self):
        return self._address

    @property
    def city(self):
        return self._city

    @property
    def state(self):
        return self._state

    @property
    def postal_code(self):
        return self._postal_code

    @property
    def employed_by(self):
        return self._employed_by

    @property
    def position(self):
        return self._position

    @property
    def salary(self):
        return self._salary

    @property
    def qualifications(self):
        return self._qualifications

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @ssn.setter
    def ssn(self, ssn):
        self._ssn = ssn

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @address.setter
    def address(self, address):
        self._address = address

    @city.setter
    def city(self, city):
        self._city = city

    @state.setter
    def state(self, state):
        self._state = state

    @postal_code.setter
    def postal_code(self, postal_code):
        self._postal_code = postal_code

    @employed_by.setter
    def employed_by(self, employed_by):
        self._employed_by = employed_by

    @position.setter
    def position(self, position):
        self._position = position

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    def add_qualification(self, qualification):
        self._qualifications.append(qualification)

    def remove_qualification(self, qualification):
        self._qualifications.remove(qualification)
