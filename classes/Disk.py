"""
Disk Class for Workstation
"""
from classes.WorkstationComponent import WorkstationComponent


class Disk(WorkstationComponent):
    def __init__(self, name, description, cost, space_required, speed, total_disk_space):
        self.total_disk_space: int = total_disk_space
        super().__init__(name, description, cost, space_required, speed)
