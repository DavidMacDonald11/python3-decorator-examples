from abc import ABC, abstractmethod
from functools import cached_property

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @classmethod
    @abstractmethod
    def count(cls):
        pass
