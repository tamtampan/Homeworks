# Zadatak 1
#
# Modelovati interfejs za primitivan fajl sistem. Fajl sistem cemo modelovati bez direktorijuma, dakle nas fajl sistem
# ima samo fajlove, datoteke. Fajlovi mogu biti razlicitog tipa, ali dele skup funkcionalnosti - svaki fajl ima naziv,
# tip (ekstenziju), velicinu, opis, trenutak (moze datum i vreme, moze samo datum, moze samo vreme, moze timestamp,
# moze samo neki arbitrarni broj - stagod hocete) poslednje modifikacije, i neki sadrzaj (dummy sadrzaj, sadrzaj svih
# fajlova moze biti modelovan prostim stringom za potrebe ovog zadatka - NE RADITI SA PRAVIM FAJLOVIMA) . Svi fajlovi
# se mogu procitati i u sve fajlove se moze upisati (read, write). Pri citanju iscitava se sadrzaj, pri upisu sadrzaj
# se menja, a menja se i trenutak poslednje modifikacije fajla (i ukoliko je potrebno jos nekih atributa datog fajla,
# zavisno od tipa).
# Od mogucih fajlova imamo:
# 1. Tekstualne tipa .txt koji pored gore navedenih atributa imaju jos i broj karaktera u njima;
# 2. Slike tipa .img koji imaju dimenzije sllike;
# 3. Video fajlove tipa .mp4 koji imaju dimenziju slike i trajanje.
#
# U mainu napraviti bar po jedan fajl svakog tipa, i pozvati/iskoristiti svaku od njihovih metoda.
#
# Cilj je dakle da imamo jasnu, cistu hijerarhiju klasa, a ne da unosimo kompleksnost radeci sa pravim fajlovima.
# Tako da obratite paznju molim vas, ko koga nasledjuje i to ce biti dovoljno da utvrdimo nasledjivanje kao koncept.
# Nikakva logicka kompleksnost ne postoji u ovom zadatku.


from txt_class import TextFile
from img_class import ImgFile
from video_class import Video

if __name__ == '__main__':
    some_text = "Prvi objektno orijentisan programski jezik (Simula) uveo je ideju o objektima.\nObjekti su skupovi " \
                "informacija koje se tretiraju kao jedinstven entitet. O tome će biti reči u nastavku teksta, ali," \
                "\npre toga potrebno je spomenuti pojam Klasa u objektno orijentisanom programiranju." \
                "\nKlase definišu objekat, odnosno one sadrže atribute i metode koje objekat treba da ima. Da bi se" \
                " kreirao objekat, potrebno\nje prethodno imati klasu. Klase, dakle, predstavljaju neku vrstu šablona," \
                " prema kome se kreiraju objekti, što nas dalje navodi \nda klase mogu imati više objekata." \
                "\nMožemo, na primer imatu klasu koja se zove Auto. Atributi predstavljaju osobine objekta - na " \
                "primeru automobila, to bi bili marka \nautomobila, boja, broj vrata itd.\nMetode predstavljaju" \
                " operacije koje objekat izvršava - na primeru automobila metode bi bile: kreni, zaustavi, ubrzaj...\n"
    text = TextFile(name="Tekst fajl", file_type=".txt", size="10MB", description="OOP programiranje",
                    content="OOP programiranje je...")
    text.write(some_text)
    print(text)
    print(text.read())

    magazine_text = "Kako ukrasiti jelku\nHaljine za docek\nKako pozirati na novogodisnjim slikama\n"
    picture_file = ImgFile(name="Slika za magazin", file_type=".img", size="15MB", description="Novogodisnja idila",
                           content="Sadrzaj naslovne strane", pic_dimension="20x35")
    picture_file.write(magazine_text)
    print(picture_file)
    print(picture_file.read())

    video_content = 'Programming at university can be fun. We found our own way to access the Python programming ' \
                    'language. Somehow. Meh. \nA song for programmers and sexy coding.\nOriginal songs covered:\n' \
                    '"Yo Home To Bel Air" by The Fresh Prince (1992)\n"U Can not Touch This" by MC Hammer (1990)\n' \
                    '"Gangnam Style" by Psy (2012)\n"Thrift Shop" by Macklemore & Ryan Lewis (2012)'
    video = Video(name="Spot", file_type=".mp4", size="100MB", description="Pesma: 'Python Programming Song'",
                  content="Neki tekst", pic_dimension="15x15", duration="6:38")
    video.write(video_content)
    print(video)
    print(video.read())
