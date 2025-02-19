from src.model.entites.enscritos import Inscritos
from abc import ABC, abstractmethod

class SubscribersRepositoryInterface(ABC):
    @abstractmethod
    def insert(self, subscriber_infos: dict) -> None:
        pass
    @abstractmethod
    def select_subscriber(self, email: str, event_id: int) -> Inscritos:
        pass