from runner_class import Runner
from jumper_class import Jumper


class Discipline:
    def __init__(self, name: str, discipline_type: str, num_of_competitors: int):
        self.name = name
        self.discipline_type = discipline_type
        self.num_of_competitors = num_of_competitors
        self.athlete_info = []

    def load_info(self):
        for competitor in range(self.num_of_competitors):
            print(f"Takmicar broj {competitor + 1}")
            name = input(f"Ime: ")
            surname = input("Prezime: ")
            score = int(input("Rezultat: "))
            if self.discipline_type.lower() == "runner":
                self.athlete_info.append(Runner(name, surname, score, self.name))
            elif self.discipline_type.lower() == "jumper":
                self.athlete_info.append(Jumper(name, surname, score, self.name))

    def get_winner_info(self):
        list_of_scores = []
        for athlete in self.athlete_info:
            list_of_scores.append(athlete.get())
        if self.discipline_type.lower() == "runner":
            index = list_of_scores.index(min(list_of_scores))
        elif self.discipline_type.lower() == "jumper":
            index = list_of_scores.index(max(list_of_scores))
        print("\nPodaci o pobedniku:")
        return self.athlete_info[index].__str__() + "\n"
