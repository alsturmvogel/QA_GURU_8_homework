from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from email_address import EmailAddress
from status import Status
from utils import clean_text

DEFAULT_SHORT_BODY_LENGTH = 10


@dataclass
class Email:
#Модель электронного письма.

    subject: str
    body: str
    sender: EmailAddress
    recipients: list[EmailAddress]
    status: Status = field(default=Status.DRAFT)
    date: Optional[str] = field(default=None)
    short_body: Optional[str] = field(default=None)

 # Пост-инициализация: нормализация recipients


    def __post_init__(self) -> None:
    # recipients принимает один адрес или список; хранится как список
        if isinstance(self.recipients, EmailAddress):
            self.recipients = [self.recipients]

# Публичные методы

    def get_recipients_str(self) -> str:
    #Возвращает строку с адресами получателей, разделёнными запятой.
        return ', '.join(str(recipient) for recipient in self.recipients)

    def clean_data(self) -> Email:
    #Очищает subject и body от лишних пробелов и переносов.
        self.subject = clean_text(self.subject)
        self.body = clean_text(self.body)
        return self

    def add_short_body(self, n: int = DEFAULT_SHORT_BODY_LENGTH) -> Email:
    #Записывает в short_body первые n символов тела письма (+ '...' если длиннее).
        if len(self.body) > n:
            self.short_body = self.body[:n] + '...'
        else:
            self.short_body = self.body
        return self

    def is_valid_fields(self) -> bool:
    #Проверяет, что subject и body не пустые.
        return bool(self.subject.strip()) and bool(self.body.strip())

    def prepare(self) -> Email:
    # Очищает subject и body,
    # проверяет заполненность обязательных полей,
    # устанавливает статус READY или INVALID,
    # формирует short_body.
        self.clean_data()
        self.add_short_body()

        has_sender = self.sender is not None
        has_recipients = bool(self.recipients)
        fields_valid = self.is_valid_fields()

        if fields_valid and has_sender and has_recipients:
            self.status = Status.READY
        else:
            self.status = Status.INVALID

        return self

# Магические методы

def __str__(self) -> str:
    recipients_str = self.get_recipients_str()
    body_text = self.short_body if self.short_body else self.body
    return (
        f'Status: {self.status}\n'
        f'Кому: {recipients_str}\n'
        f'От: {self.sender.masked}\n'
        f'Тема: {self.subject}, дата {self.date}\n'
        f'{body_text}'
        )