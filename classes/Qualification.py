"""
Employee Qualifications class
"""


class Qualification:
    def __init__(self, title, level):
        self.title: str = title
        self.level: str = level

    def __str__(self):
        return (
            f"{self.title}, {self.level}"
        )
