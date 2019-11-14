"""
Workstation Class
"""

from classes import WorkstationComponent


class Workstation:
    def __init__(self, name, description, cost, total_space, components):
        self.name: str = name
        self.description: str = description
        self.cost: float = cost
        self.total_space: int = total_space
        # TODO: Map out total space requirements per component
        self.components: list[WorkstationComponent] = components
