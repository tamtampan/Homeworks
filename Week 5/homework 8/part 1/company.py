"""Model for describing companies."""

import typing as t
from employee import Employee
from employee_datetime import HOURS_PER_DAY, DAYS_PER_MONTH, MONTHS_PER_YEAR


class Company:
    """Model for company."""

    def __init__(self, pib: str, name: str, employees: t.List[Employee] = []) -> None:
        """Initialize the Company object."""
        self.pib = pib
        self.name = name
        self.employees = employees

    def hire_employee(self, employee: Employee) -> None:
        """Hire an employee."""
        if self.find_employee_by_jmbg(employee.jmbg):
            raise Exception("We already have that employee employed!")
        else:
            self.employees.append(employee)
            print(f"Zaposlen je radnik {employee.name}.")

    def find_employee_by_jmbg(self, jmbg: str):
        """Find employee by jmbg if exists in list of employees."""
        for e in self.employees:
            if e.jmbg == jmbg:
                return e

        return None

    def calculate_total_monthly_outcome(self) -> int:
        """Calculate monthly outcome for all employees."""
        monthly_outcome = 0
        for em in self.employees:
            monthly_outcome += em.calculate_monthly_income()
        return monthly_outcome

    def calculate_total_annual_outcome(self) -> int:
        """Calculate annual outcome for all employees."""
        return self.calculate_total_monthly_outcome() * MONTHS_PER_YEAR

    def fire_employee(self, employee: Employee) -> None:
        """Fire an employee."""
        if self.find_employee_by_jmbg(employee.jmbg):
            self.employees.remove(employee)
            print(f"Otpustili ste radnika {employee.name}.")
        else:
            raise Exception("We do not have that employee employed!")

    def get_all_positions(self) -> list:
        """Get all positions in company."""
        positions = []
        for e in self.employees:
            if e.position not in positions:
                positions.append(e.position)
        return positions

    # s obzirom da u zadatku nije naglaseno da li se trazi prosecna satnica, mesecna postrosnja ili godisnja
    # potrosnja za odredjenu poziciju u kompaniji, napravila sam 3 funkcije:
    def calculate_position_outcome_hourly(self, position: str) -> float:
        """Calculate average hourly outcome for all employees on specific position. """
        total_position_outcome = []
        for e in self.employees:
            if e.position == position:
                total_position_outcome.append(e.hourly)
        try:
            result = sum(total_position_outcome) / len(total_position_outcome)
            return result
        except ZeroDivisionError:
            print("We do not have that position in company.")

    def calculate_position_outcome_monthly(self, position: str) -> int:
        """Calculate monthly outcome for all employees on specific position."""
        total_position_outcome = []
        for e in self.employees:
            if e.position == position:
                total_position_outcome.append(e.hourly * HOURS_PER_DAY * DAYS_PER_MONTH)
        if sum(total_position_outcome) != 0:
            return sum(total_position_outcome)
        else:
            raise Exception("We do not have that position in company.")

    def calculate_position_outcome_annual(self, position: str) -> int:
        """Calculate annual outcome for all employees on specific position."""
        return self.calculate_position_outcome_monthly(position) * MONTHS_PER_YEAR

    def change_hourly(self, employee: Employee, new_hourly: int) -> None:
        if self.find_employee_by_jmbg(employee.jmbg):
            employee.hourly = new_hourly
            print(f"Nova satnica za {employee.name} je {new_hourly} evra.")
        else:
            raise Exception("We do not have that employee employed!")
