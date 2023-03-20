# Zadatak 2
#
# Implementirati aplikaciju takmičenje u atletskim disciplinama.
# Kreirati apstraktnu klasu Athlete čiji su javni atributi ime i prezime, a privatni
# rezultat ostvaren na takmičenju. Metode koje atletičar ima su:
# ● Apstraktna metoda koja ispituje da li je rezultat atletičara bolji od rezultata
# drugog atletičara
# ● Metoda koja učitava podatke o atletičaru iz konzole (input)
# ● Metoda za prikaz podataka o atletičaru u konzoli
#
# Kreirati klase Runner i Jumper koje su izvedene iz klase Athlete. Kod trkača je bolji manji
# rezultat, dok je kod skakača bolji veći rezultat.
# Kreirati klasu Discipline, čiji su privatni atributi:
# ● Ime discipline, tip discipline (poželjno da bude enumeracija sa vrednostima
# RUNNING, JUMPING), broj učesnika i niz podataka o atletičarima, učesnicima
# discipline. Definisati metode:
# ○ init metodu koja postavlja ime discipline, tip i broj učesnika
# ○ metoda koja učitava podatke o učesnicima iz konzole
# ○ Metoda koja prikazuje podatke o pobedniku u disciplini
# U glavnom delu programa kreirati discipline ‘Long jump’ i ‘100m sprint’ sa proizvoljnim
# brojem učesnika, učitati podatke o učesnicima obe discipline iz konzole i prikazati poruke
# o pobednicima obe discipline.

from discipline_class import Discipline


def competition():
    long_jump = Discipline("Long jump", "jumper", 3)
    long_jump.load_info()
    print(long_jump.get_winner_info())
    sprint_100m = Discipline("100m sprint", "runner", 2)
    sprint_100m.load_info()
    print(sprint_100m.get_winner_info())


if __name__ == '__main__':
    competition()
