# Potreban nam je program pomoću kojeg ćemo pratiti uspeh studenata na ispitima. Za
# svakog studenta pamtimo ime, prezime, broj indeksa, smer i sve predmete koje
# treba da položi ili je položio sa ocenom od 6 do 10.
# Za svaki smer pamtimo ime smera, modul na kome je taj smer, listu predmeta koje taj smer moze imati kao
# i sve studente na tom smeru.
# Za svaki predmet pamtimo naziv i jedinstvenu šifru predmeta.
# Na osnovu unetih podataka, potrebno je da program omogući prikaz (ima sledeće funkcionalnosti):
# a) dodavanje novog studenta na smer
# b) dodavanje novog predmeta na smer
# c) dodavanje novog predmeta studentu
# d) listu svih položenih ispita određenog studenta
# e) srednje ocene određenog studenta
# f) podataka studenta/studenata sa najvećom prosečnom ocenom
# g) podataka studenta/studenata sa najmanje položenih ispita
# h) svih studenta koji su položili sve ispite na predmetima koji su im dodeljeni
# i) raspodele studenata po smerovima, u procentima
# j) sve studente na odabranom smeru
# k) najboljeg studenta na odabranom smeru
# l) sve predmete koje nije položio niti jedan student
# m) predmeta sa najvećom prosečnom ocenom
# Kada se program pokrene, prikazati korisniku glavni meni sa opcijama a - m (koje može
# da unese sa tastature). Nakon odabira opcije, ukoliko je potrebno, od korisnika
# zahtevati unos podataka i prikazati željene rezultate. Potom, ponovo prikazati glavni
# Meni.Korisnik prekida program odabirom opcije “Kraj programa”
#
# Koristiti specijalne metode gde je moguce.
# Koristiti enkapsulaciju tamo gde je potrebno.
# Koristiti engleski jezik.
# Za svaku klasu praviti poseban fajl.


from department import Department
from student import Student
from subject import Subject
from faculty import Faculty


def main():
    fmu = Faculty("Fakultet muzicke umetnosti")
    subject_1 = Subject("Flauta 1", "FL01")
    subject_2 = Subject("Orkestarske deonice 1", "OD01")
    subject_3 = Subject("Kamerna muzika 1", "KM01")
    subject_4 = Subject("Solfedjo 1", "SO01")
    subject_5 = Subject("Violina 1", "VI01")
    subject_6 = Subject("Klavir 1", "KL01")
    subject_7 = Subject("Dirigovanje 1", "DI01")
    subject_8 = Subject("Istorija muzike 1", "IM01")
    subject_9 = Subject("Pedagogija 1", "PE01")
    subject_10 = Subject("Psihologija 1", "PS01")
    subject_11 = Subject("Sociologija 1", "SO01")
    subject_12 = Subject("Truba 1", "TR01")

    department_1 = Department("Duvacki instrumenti", "VII", fmu,
        [subject_1, subject_2, subject_3, subject_4, subject_8, subject_9, subject_10, subject_11, subject_12])
    department_2 = Department("Gudacki instrumenti", "VI", fmu,
        [subject_5, subject_2, subject_3, subject_4, subject_8, subject_9, subject_10, subject_11])
    department_3 = Department("Polifoni instrumenti", "V", fmu,
        [subject_6, subject_7, subject_3, subject_4, subject_8, subject_9, subject_10, subject_11])

    student_1 = Student("Marko", "Markovic", "1001", department_1, [subject_1, subject_2, subject_3])
    student_2 = Student("Strahinja", "Radojicic", "1002", department_2, [subject_2, subject_3, subject_4, subject_5, subject_11])
    student_3 = Student("Jelena", "Jovanovic", "1003", department_3, [subject_6, subject_7, subject_3, subject_4, subject_10])
    student_4 = Student("Milica", "Stankovic", "1004", department_1, [subject_1, subject_2, subject_3, subject_4, subject_8, subject_9, subject_10, subject_11, subject_12])
    student_5 = Student("Jovana", "Blagojevic", "1005", department_1, [subject_1, subject_2, subject_3, subject_4, subject_8, subject_9, subject_10])
    student_6 = Student("Matija", "Bogdanovic", "1006", department_2, [subject_5, subject_2, subject_3, subject_4, subject_8, subject_9, subject_10, subject_11])
    student_7 = Student("Marta", "Djordjevic", "1007", department_3, [subject_6, subject_7, subject_3, subject_4])
    student_1.add_grade(subject_1.name, 10, fmu)
    student_1.add_grade(subject_2.name, 8, fmu)
    student_1.add_grade(subject_3.name, 10, fmu)
    student_2.add_grade(subject_2.name, 9, fmu)
    student_4.add_grade(subject_1.name, 10, fmu)
    student_6.add_grade(subject_10.name, 6, fmu)
    student_7.add_grade(subject_6.name, 8, fmu)
    student_3.add_grade(subject_4.name, 7, fmu)
    student_7.add_grade(subject_7.name, 8, fmu)
    student_6.add_grade(subject_8.name, 9, fmu)
    student_4.add_grade(subject_3.name, 10, fmu)
    department_1.add_student(student_1)
    department_1.add_student(student_4)
    department_1.add_student(student_5)
    department_2.add_student(student_2)
    department_2.add_student(student_6)
    department_3.add_student(student_3)
    department_3.add_student(student_7)

    option = input("Izaberite opciju a/b/c/d/e/f/g/h/i/j/k/l/m: ").lower()
    while option != "kraj programa":
        if option == "a":
            new_student = input("Napisite ime, prezime, indeks studenta kojeg zelite upisati (odvojite razmakom podatke): ")
            list_of_info = new_student.split()
            while len(list_of_info) != 3:
                new_student = input("Pokusajte ponovo: ")
                list_of_info = new_student.split()
            departments = fmu.get_all_departments()
            wanted_department = input("U koji smer zelite upisati studenta? ").lower()
            while wanted_department not in departments:
                wanted_department = input("Morate izabrati jedan od ponudjenih smerova: ").lower()
            for department in fmu.departments:
                if department.name.lower() == wanted_department:
                    department.add_student(Student(new_student[0], new_student[1], new_student[2], department, []))
                    print(f"Student je uspesno upisan na smer '{department.name}'.")
        elif option == "b":
            new_subject = input("Napisite ime i sifru premeta kojeg zelite dodati (odvojite razmakom podatke): ")
            list_of_info = new_subject.split()
            while len(list_of_info) != 2:
                new_subject = input("Pokusajte ponovo: ")
                list_of_info = new_subject.split()
            departments = fmu.get_all_departments()
            wanted_department = input("U koji smer zelite dodati predmet? ").lower()
            while wanted_department not in departments:
                wanted_department = input("Morate izabrati jedan od ponudjenih smerova: ").lower()
            for department in fmu.departments:
                if department.name.lower() == wanted_department:
                    department.add_subject(Subject(new_subject[0], new_subject[1]))
                    print(f"Predmet je uspesno dodat na smer '{department.name}'.")
        elif option == "c":
            id_list = fmu.get_all_students_ids()
            answer = input("Izaberite indeks studenta: ")
            while answer not in id_list:
                answer = input("Pogresan unos, pokusajte ponovo: ")
            print("Predmeti na smeru studenta.")
            for department in fmu.departments:
                for student in department.students:
                    if student.student_id == answer:
                        wanted_student = student
            print(wanted_student.department)
            answer = input("Koji predmet zelite dodati studentu? ").lower()
            for subject in wanted_student.department.subjects:
                if subject.name.lower() == answer:
                    if subject not in wanted_student.subjects:
                        wanted_student.add_subject(subject)
                        print("Predmet je uspesno dodeljen.")
                    else:
                        print("Studentu je vec dodeljen ovaj predmet.")

        elif option == "d":
            id_list = fmu.get_all_students_ids()
            answer = input("Izaberite indeks studenta za listu njegovih ispita: ")
            while answer not in id_list:
                answer = input("Pogresan unos, pokusajte ponovo: ")
            for department in fmu.departments:
                for student in department.students:
                    if student.student_id == answer:
                        list_of_passed_exams = student.get_all_passed_exams()
            string_to_print = "Polozeni ispiti ovog studenta: "
            if len(list_of_passed_exams) == 0:
                print("Student nije polozio niti jedan ispit.")
            else:
                for exam in list_of_passed_exams:
                    for exam_name in exam:
                        string_to_print += f"{exam_name}, "
                print(string_to_print[:-2])
        elif option == "e":
            id_list = fmu.get_all_students_ids()
            answer = input("Izaberite indeks studenta za izracunavanje proseka: ")
            while answer not in id_list:
                answer = input("Pogresan unos, pokusajte ponovo: ")
            for department in fmu.departments:
                for student in department.students:
                    if student.student_id == answer:
                        print(student.average_student_grade())
        elif option == "f":
            print("Studenti sa najvecim prosekom u svakom smeru:\n")
            for department in fmu.departments:
                student_highest = department.get_student_with_highest_average()
                for student in student_highest:
                    print(f"{student}")
        elif option == "g":
            print("Studenti sa najmanje polozenih ispita u svakom smeru:\n")
            for department in fmu.departments:
                students_list = department.get_student_with_least_passed_exams()
                for student in students_list:
                    print(student)
        elif option == "h":
            print("Studenti koji su polozili sve ispite:\n")
            for department in fmu.departments:
                all_passed = department.get_students_with_all_exams_passed()
                for student in all_passed:
                    print(student)
        elif option == "i":
            print(fmu.get_percentage_distribution_by_departments())
        elif option == "j":
            names_of_departments = fmu.get_all_departments()
            print("Za koji smer zelite prikaz svih studenata?")
            department_input = input("Izaberite smer: ").lower()
            while department_input not in names_of_departments:
                department_input = input("Pogresan unos, pokusajte ponovo: ").lower()
            print("Studenti na ovom smeru:")
            for department in fmu.departments:
                if department.name.lower() == department_input:
                    for student in department.students:
                        print(student)
        elif option == "k":
            names_of_departments = fmu.get_all_departments()
            department_input = input("Izaberite smer: ").lower()
            while department_input not in names_of_departments:
                department_input = input("Pogresan unos, pokusajte ponovo: ").lower()
            print("Najbolji student/studenti na ovom smeru:")
            for department in fmu.departments:
                if department.name.lower() == department_input:
                    for best_score in department.get_student_with_highest_average():
                        print(best_score)
        elif option == "l":
            subjects_list = fmu.get_unpassed_exams(self=fmu)
            string_to_print = "Predmeti koje nije polozio niti jedan student: "
            for subject in subjects_list:
                string_to_print += f"{subject}, "
            print(string_to_print[:-2])
        elif option == "m":
            string_to_print = "Predmeti sa najvecom prosecnom ocenom: "
            subjects_dict = fmu.get_subject_with_highest_average(self=fmu)
            for subject in subjects_dict:
                string_to_print += f"{subject} (prosek: {round(subjects_dict[subject], 2)}), "
            print(string_to_print[:-2])
        else:
            if option != "kraj programa":
                print("Pogresan unos, pokusajte ponovo.")
        option = input("Izaberite opciju a/b/c/d/e/f/g/h/i/j/k/l/m: ").lower()


if __name__ == '__main__':
    print("a) dodavanje novog studenta na smer\nb) dodavanje novog predmeta na smer\n"
          "c) dodavanje novog predmeta studentu\nd) listu svih položenih ispita određenog studenta\n"
          "e) srednje ocene određenog studenta\nf) podataka studenta/studenata sa navećom prosečnom ocenom\n"
          "g) podataka studenta/studenata sa najmanje položenih ispita\n"
          "h) svih studenta koji su položili sve ispite na predmetima koji su im dodeljeni\n"
          "i) raspodele studenata po smerovima, u procentima\nj) sve studente na odabranom smeru\n"
          "k) najboljeg studenta na odabranom smeru\nl) sve predmete koje nije položio niti jedan student\n"
          "m) predmeta sa najvećom prosečnom ocenom\nZa kraj: KRAJ PROGRAMA")
    main()
    print("Bye :)")
