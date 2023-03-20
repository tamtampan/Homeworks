import datetime


class File:

    def __init__(self, name: str, file_type: str, size: str, description: str, content: str) -> None:
        self.name = name
        self.file_type = file_type
        self.size = size
        self.description = description
        self.content = content
        self.date = datetime.datetime.now().date()
        self.time = datetime.datetime.now().time()

    def read(self) -> str:
        return f"Tekst fajla:\n{self.content}"

    def write(self, new_content) -> None:
        self.content = new_content
        self.date = datetime.datetime.now().date()
        self.time = datetime.datetime.now().time()

    def __str__(self):
        return f"Ime fajla: {self.name}, Tip fajla: {self.file_type}, Velicina: {self.size}\nOpis fajla: " \
               f"{self.description}\nVreme i datum poslednje izmene: {self.time}, {self.date}"
