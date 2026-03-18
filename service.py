from __future__ import annotations

import copy
from datetime import date

from email_model import Email
from status import Status


class EmailService:  # Сервис имитации отправки электронных писем.

    def __init__(self, email: Email) -> None:
        self._email = email

    # Публичные методы

    @staticmethod
    def add_send_date() -> str:
        # Возвращает текущую дату в формате YYYY-MM-DD.
        return date.today().isoformat()

    def send_email(self) -> list[Email]:
        # Имитирует отправку письма.
        # Returns: список новых писем (одно на получателя) со статусом SENT или FAILED.

        sent_emails: list[Email] = []

        for recipient in self._email.recipients:
            new_email: Email = copy.deepcopy(self._email)

            new_email.recipients = [recipient]
            new_email.date = self.add_send_date()

            new_email.status = (
                Status.SENT if self._email.status == Status.READY else Status.FAILED
            )

            sent_emails.append(new_email)

        return sent_emails
