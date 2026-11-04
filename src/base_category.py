from abc import ABC, abstractmethod

class BaseCategory(ABC):
    """Родитель Category and Order"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def total_cost(self):
        pass
