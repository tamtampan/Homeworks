from abc import ABC
from athlete_class import Athlete


class Jumper(Athlete, ABC):
    def __init__(self, name: str, surname: str, score: float, discipline: str):
        super().__init__(name, surname, score)
        self.discipline = discipline

    def is_better_than_other(self, other: 'Jumper'):
        if self.get() > other.get():
            return True
        elif self.get() < other.get():
            return False
        else:
            return None

    def load_athlete(self):
        name = input("Ime:")
        surname = input("Prezime: ")
        score = int(input("Rezultat: "))
        return Jumper(name, surname, score, self.discipline)

    def __str__(self):
        return f"Ime i prezime takmicara: {self.name} {self.surname}\nDisciplina: {self.discipline}, Rezultat: {self.get()}"
