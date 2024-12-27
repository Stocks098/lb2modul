class Book:
    """базовый класс книги"""

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"книга {self.name}. автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("кол-во страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("кол-во страниц должно быть положительным числом.")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()}, {self.pages} страниц."


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("продолжительность должна быть числом с плавающей точкой.")
        if value <= 0:
            raise ValueError("продолжительность должна быть положительынм числом.")
        self._duration = value

    def __str__(self):
        return f"{super().__str__()}, длительность {self.duration:.2f} часов."


# пример использования
try:
    book1 = PaperBook("Тихий Дон", "М.Шолохов", 1909)
    print(book1)
    book2 = AudioBook("Собачье сердце", "М.Булгаков", 624.7)
    print(book2)

    # проверка ошибок
    book3 = PaperBook("Роковые яйца", "М. Булгаков", -23)
except (TypeError, ValueError) as e:
    print(e)
