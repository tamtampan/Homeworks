"""Model for describing students."""
import typing as t
from subject import Subject
from faculty import Faculty


class Student:
    """Model for students."""

    def __init__(self, name: str, surname: str, student_id: str, department, subjects: t.List[Subject]) -> None:
        """Initialize the Student object."""
        self.__name = name
        self.__surname = surname
        self.student_id = student_id
        self.department = department
        self.subjects = subjects
        self.grades = {}
        for subject in self.subjects:
            self.grades[subject.name] = None

    def __str__(self) -> str:
        """Get informations about object."""
        result = f"Ime i prezime: {self.__name} {self.__surname}, Indeks: {self.student_id}, " \
                 f"Smer: {self.department.name}\nPredmeti:\n"
        for subject in self.subjects:
            result += subject.name + "\n"
        return result

    # c) dodavanje novog predmeta studentu
    def add_subject(self, new_subject: Subject) -> None:
        """Add Subject to Student list of subjects."""
        if new_subject not in self.subjects:
            self.subjects.append(new_subject)
            self.grades[new_subject.name] = None

    def add_grade(self, subject_name, grade: int, faculty: Faculty) -> None:
        """Add grade to Student."""
        self.grades[subject_name] = grade
        if subject_name not in faculty.all_grades:
            faculty.all_grades[subject_name] = [grade]
        else:
            faculty.all_grades[subject_name].append(grade)

    def get_name(self) -> str:
        return self.__name

    # d) listu svih položenih ispita određenog studenta
    def get_all_passed_exams(self) -> t.List[dict]:
        """Get list of passed exams."""
        list_of_passed_exams = []
        for grade in self.grades:
            if self.grades[grade] is not None:
                list_of_passed_exams.append({grade: self.grades[grade]})
        return list_of_passed_exams

    # e) srednje ocene određenog studenta
    def average_student_grade(self):
        """Get average grade of Student."""
        passed_exams = self.get_all_passed_exams()
        sum_of_grades = 0
        total_num_of_passed_exams = len(passed_exams)
        for exam in passed_exams:
            for exam_name in exam:
                sum_of_grades += exam[exam_name]
        try:
            return round(sum_of_grades/total_num_of_passed_exams, 2)
        except ZeroDivisionError:
            return 0
