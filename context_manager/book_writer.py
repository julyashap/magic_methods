from config import BOOKS_PATH
from datetime import date

class BookWriter:
    def __init__(self, title):
        self.title = title
        self.path = BOOKS_PATH.joinpath(self.title)

    def __enter__(self):
        if not self.path.exists():
            self.path.mkdir(parents=True)
        self.page = 1
        return self

    def add_page(self, text):
        page_path = self.path.joinpath(f"{self.page}.txt")
        with open(page_path, 'w', encoding='utf-8') as file:
            file.write(text)
        self.page += 1

    def __exit__(self, exc_type, exc_value, exc_tb):
        credits_path = self.path.joinpath("credits.txt")
        with open(credits_path, 'w', encoding='utf-8') as file:
            file.write(f"Автор: я\n"
                       f"Дата: {date.today()}\n"
                       f"Страницы: {self.page - 1}")
