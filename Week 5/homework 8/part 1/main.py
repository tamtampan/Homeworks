# Ili modelovati zaposlenog u nekoj firmi. Jedan zaposljeni radi samo u jednoj firmi,
# a jedna firma ima vise zaposljenih. Zaposljeni (Employee) ima ime, prezime, JMBG, satnicu,
# i naziv funkcije koju obavlja (racunovodstvo, menadzment, radnici na traci, inzenjeri recimo).
# Za svakog se moze izracunati koliko iznosi njegova plata na godisnjem i na mesecnom nivou.

# Firma ima PIB i naziv. Jedna firma moze izracunati koliko ukupno placa svoje zaposlene na
# godisnjem i mesecnom nivou. Firma moze otpustiti zaposlenog ili zaposliti novog. Firma moze
# prikazati koje sve funkcije obavljaju njeni zaposleni. Firma moze izracunati koliko trosi na
# zaposlene na datoj funkciji. Za svakog zaposlenog se moze povecati ili smanjiti satnica.
# (Deo koda koji smo uradili na predavanjima bice u fajlovima u ovom direktorijumu!
# Obratiti paznju i iskoristiti funkciju find_employee_by_jmbg u funkciji hire_employee.)
#
#  Modelovati tacku, duz i cetvorougao.
# Tacka ima dve celobrojne koordinate, po x i po y osi. Mozemo promeniti koordinate jedne tacke.
# Duz ima pocetnu i krajnju tacku, i duzinu (ne morate izracunavati duzinu na osnovu koordinata,
#                                                                                    nema potrebe).
# Pocetna i krajnja tacka, kao i duzina se mogu menjati.
# Cetvorougao ima 2 duzi, a i b. Mozemo mu izracunati obim (O = 2*a + 2*b, gde su a i b duzi koje
# opisuju cetvorougao, respektivno), i povrsinu (P=a*b, a i b su duzi koje opisuju cetvorougao).

from company import Company
from employee import Employee

if __name__ == '__main__':
    employee1 = Employee(name="Pera", surname="Peric", jmbg="0304998765020", hourly=20, position="Cook")
    employee2 = Employee(name="Milan", surname="Milutinovic", jmbg="2009992000000", hourly=25, position="Waiter")
    employee3 = Employee(name="Jovana", surname="Jovanovic", jmbg="0912963000000", hourly=30, position="Cook")
    restaurant = Company(pib="123456789", name="Restaurant")

    # Zaposljavanje
    restaurant.hire_employee(employee1)
    restaurant.hire_employee(employee2)
    restaurant.hire_employee(employee3)

    # Za svakog se moze izracunati koliko iznosi njegova plata na godisnjem i na mesecnom nivou.
    print(f"Mesecna plata radnika {employee1.name} je {employee1.calculate_monthly_income()} evra.")
    print(f"Mesecna plata radnika {employee2.name} je {employee2.calculate_monthly_income()} evra.")
    print(f"Mesecna plata radnika {employee3.name} je {employee3.calculate_monthly_income()} evra.")
    print(f"Godisnja plata radnika {employee1.name} je {employee1.calculate_annual_income()} evra.")
    print(f"Godisnja plata radnika {employee2.name} je {employee2.calculate_annual_income()} evra.")
    print(f"Godisnja plata radnika {employee3.name} je {employee3.calculate_annual_income()} evra.")

    # Jedna firma moze izracunati koliko ukupno placa svoje zaposlene na
    # godisnjem i mesecnom nivou.
    print(f"Mesecno placanje svih radnika u restoranu {restaurant.name} je "
          f"{restaurant.calculate_total_monthly_outcome()} evra.")
    print(f"Mesecno placanje svih radnika u restoranu {restaurant.name} je "
          f"{restaurant.calculate_total_annual_outcome()} evra.")

    # Firma moze otpustiti zaposlenog ili zaposliti novog.
    restaurant.fire_employee(employee1)

    # Firma moze prikazati koje sve funkcije obavljaju njeni zaposleni.
    print("Sve pozicije u restoranu:")
    print(restaurant.get_all_positions())

    # Firma moze izracunati koliko trosi na zaposlene na datoj funkciji.
    print(f"Mesecno placanje na specificnoj poziciji je {restaurant.calculate_position_outcome_monthly('Cook')} evra.")
    print(f"Godisnje placanje na specificnoj poziciji je {restaurant.calculate_position_outcome_annual('Cook')} evra.")

    # Za svakog zaposlenog se moze povecati ili smanjiti satnica.
    restaurant.change_hourly(employee2, 100)
