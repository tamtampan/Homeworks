"""Model for describing faculty."""


class Faculty:
    """Model for faculty."""

    def __init__(self, name: str) -> None:
        """Initialize the Faculty object."""
        self.name = name
        self.all_grades = {}
        self.departments = []

    # i) raspodele studenata po smerovima, u procentima
    def get_percentage_distribution_by_departments(self) -> str:
        """Get percentage of students in every department."""
        sum_all_students = 0
        students_in_departments = {}
        string_to_print = "Procentualna rasprostranjenost sudenata po smerovima je: "
        for department in self.departments:
            students_in_departments[department.name] = len(department.students)
            sum_all_students += len(department.students)
        for d in students_in_departments:
            string_to_print += f"{d} - {round(students_in_departments[d] / sum_all_students * 100)}%, "
        return string_to_print[:-2]

    def get_all_students_ids(self) -> list:
        """Get id of every student."""
        string_to_print = "Indeksi svih studenata na fakultetu: "
        id_list = []
        for department in self.departments:
            for student in department.students:
                string_to_print += f"{student.student_id}, "
                id_list.append(student.student_id)
        print(string_to_print[:-2])
        return id_list

    # l) sve predmete koje nije položio niti jedan student
    @staticmethod
    def get_unpassed_exams(self) -> list:
        """Get exams that no student had passed."""
        all_unpassed_exams = []
        for department in self.departments:
            for subject in department.subjects:
                if subject.name not in all_unpassed_exams and subject.name not in self.all_grades:
                    all_unpassed_exams.append(subject.name)
        return all_unpassed_exams

    # m) predmeta sa najvećom prosečnom ocenom
    @staticmethod
    def get_subject_with_highest_average(self) -> dict:
        """Get subject with the highest average grade."""
        highest_average = 0
        exams_with_highest_average = {}
        for exam in self.all_grades:
            current_average = sum(self.all_grades[exam]) / len(self.all_grades[exam])
            if current_average > highest_average:
                highest_average = current_average
                exams_with_highest_average.clear()
                exams_with_highest_average[exam] = current_average
            if current_average == highest_average:
                exams_with_highest_average[exam] = current_average
        return exams_with_highest_average

    def get_all_departments(self) -> list:
        """Get list of all departments names."""
        departments = self.departments
        names_of_departments = []
        string_to_print = "Smerovi na fakultetu: "
        for d in departments:
            string_to_print += f"{d.name}, "
            names_of_departments.append(d.name.lower())
        print(string_to_print[:-2])
        return names_of_departments
