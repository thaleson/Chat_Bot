# chatbot_interface.py
from abc import ABC, abstractmethod

class ChatbotInterface(ABC):
    @abstractmethod
    def responder(self, mensagem: str) -> str:
        pass
