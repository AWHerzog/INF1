from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def get_remaining_range(self) -> float:
        pass

    @abstractmethod
    def drive(self, dist) -> float:
        pass