"""
Workstation Component Base Class
"""


class WorkstationComponent:
    def __init__(self, name, description, cost, space_required, speed):
        self.name: str = name
        self.description: str = description
        self.cost: float = cost
        self.space_required: int = space_required
        self.speed: float = speed
