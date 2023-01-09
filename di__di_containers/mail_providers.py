from abc import ABC, abstractmethod


class MailProvider(ABC):
    @abstractmethod
    def send(self, to: str, subject: str, message: str):
        pass


class MailgunProvider(MailProvider):
    def send(self, to: str, subject: str, message: str):
        print(f'Sent email to {to} using {self.__class__.__name__}')


class UnioneProvider(MailProvider):
    def send(self, to: str, subject: str, message: str):
        print(f'Sent email to {to} using {self.__class__.__name__}')


class Mail:
    def __init__(self, provider: MailProvider):
        self._provider = provider

    def send(self, to: str, subject: str, message: str):
        self._provider.send(to=to, subject=subject, message=message)
 