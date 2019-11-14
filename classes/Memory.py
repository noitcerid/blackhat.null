"""
Memory Class for Workstation
"""
from classes.WorkstationComponent import WorkstationComponent


class Memory(WorkstationComponent):
    def __init__(self, name, description, cost, space_required, speed, total_size):
        self.total_size: int = total_size
        super().__init__(name, description, cost, space_required, speed)
