class EmailAddress:
    # Класс инкапсулирует строковый email и операции над ним

    ALLOWED_DOMAINS = ('.com', '.ru', '.net')

    def __init__(self, address: str):
        normalized = self.normalize_address(address)
        if not self.__check_correct_email(normalized):
            raise ValueError(
                f"""Невалидный email-адрес: '{address}'. Адрес должен содержать '@' и заканчиваться на {', '.join(self.ALLOWED_DOMAINS)}."""
            )
        self._address = normalized

    @property
    def address(self):
        # Возвращает нормализованный адрес.
        return self._address

    @property
    def masked(self):
        # Маска вида: первые 2 символа + '***@' + домен.
        local, domain = self._address.split("@")
        return f"{local[:2]}***@{domain}"

    @staticmethod
    def normalize_address(address: str):
        # Приводит адрес к нижнему регистру и обрезает пробелы.
        return address.lower().strip()

    def __check_correct_email(self, address: str) -> bool:
        # Проверяет корректность адреса: наличие '@' и допустимый домен.
        if "@" not in address:
            return False
        return any(address.endswith(domain) for domain in self.ALLOWED_DOMAINS)

        # Магические методы
    def __repr__(self) -> str:
        return f"EmailAddress(address='{self._address}')"

    def __str__(self) -> str:
        return self._address

    def __eq__(self, other: object) -> bool:
        if isinstance(other, EmailAddress):
            return self._address == other._address
        return NotImplemented
