"""
Mission Class
"""


class Mission:
    def __init__(self, subject, body, reward, rating_factor):
        self.subject: str = subject
        self.body: str = body
        self.reward: int = reward
        self.rating_factor: int = rating_factor
