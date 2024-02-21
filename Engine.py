from abc import ABC


class Engine(ABC):
    @abstractmethod
    def needs_service(self):
        pass

