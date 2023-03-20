from abc import ABC, abstractmethod


class Athlete(ABC):

    def __init__(self, name: str, surname: str, score: float = 0):
        self.name = name
        self.surname = surname
        self.__score = score

    def get(self):
        return self.__score

    def set(self, new_score: float):
        self.__score = new_score

    @abstractmethod
    def is_better_than_other(self, other: "Athlete"):
        pass

    def __str__(self):
        return f"Ime i prezime takmicara: {self.name} {self.surname}"

    @staticmethod
    def load_athlete(self):
        name = input("Ime:")
        surname = input("Prezime: ")
        try:
            score = int(input("Rezultat: "))
        except TypeError:
            print("Rezultat mora biti broj.")
            return None
        return name, surname, score
