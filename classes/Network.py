"""
Network Class for Workstation
"""
from classes.WorkstationComponent import WorkstationComponent


class Network(WorkstationComponent):
    def __init__(self, name, description, cost, space_required, speed, bandwidth):
        self.bandwidth: int = bandwidth
        super().__init__(name, description, cost, space_required, speed)
