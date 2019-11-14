"""
Processor Class for Workstation
"""
from classes.WorkstationComponent import WorkstationComponent


class Processor(WorkstationComponent):
    def __init__(self, name, description, cost, space_required, speed):
        super().__init__(name, description, cost, space_required, speed)
