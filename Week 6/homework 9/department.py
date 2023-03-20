"""Model for describing departments."""
import typing as t
from subject import Subject
from student import Student
from faculty import Faculty


class Department:
    """Model for departments."""

    def __init__(self, name: str, module: str, faculty: Faculty, subjects: t.List[Subject]) -> None:
        """Initialize the Department object."""
        self.name = name
        self.module = module
        self.subjects = subjects
        self.students = []
        faculty.departments.append(self)

    # a) dodavanje novog studenta na smer
    def add_student(self, new_student: Student) -> None:
        """Add Student object to list."""
        if new_student not in self.students:
            self.students.append(new_student)

    # b) dodavanje novog predmeta na smer
    def add_subject(self, new_subject: Subject) -> None:
        """Add Subject object to list."""
        if new_subject not in self.subjects:
            self.subjects.append(new_subject)

    # f) podataka studenta/studenata sa navećom prosečnom ocenom
    def get_student_with_highest_average(self) -> list:
        """Get Student objects with highest average grade."""
        best_students = []
        best_average = 0
        for student in self.students:
            if student.average_student_grade() == best_average:
                best_students.append(student)
            try:
                if student.average_student_grade() > best_average:
                    best_students.clear()
                    best_students.append(student)
                    best_average = student.average_student_grade()
            except TypeError:
                pass
        return best_students

    # g) podataka studenta/studenata sa najmanje položenih ispita
    def get_student_with_least_passed_exams(self) -> list:
        """Get Student objects with at least number of passed exams."""
        num_of_non_passed = 0
        students = []
        for student in self.students:
            if len(student.subjects) - len(student.get_all_passed_exams()) == num_of_non_passed:
                students.append(student)
            if len(student.subjects) - len(student.get_all_passed_exams()) > num_of_non_passed:
                students.clear()
                students.append(student)
                num_of_non_passed = len(student.subjects) - len(student.get_all_passed_exams())
        return students

    # h) svih studenta koji su položili sve ispite na predmetima koji su im dodeljeni
    def get_students_with_all_exams_passed(self) -> list:
        """Get Student objects with all passed exams."""
        students = []
        for student in self.students:
            if len(student.subjects) - len(student.get_all_passed_exams()) == 0 and len(student.subjects) != 0:
                students.append(student)
        return students

    def __str__(self) -> str:
        """Get information about object Department."""
        string_to_print = f"Smer: {self.name}, Modul: {self.module}\nPredmeti:\n"
        for subject in self.subjects:
            string_to_print += f"{subject.name}\n"
        return string_to_print
