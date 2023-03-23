# Modelovati tacku, duz i cetvorougao.
# Tacka ima dve celobrojne koordinate, po x i po y osi. Mozemo promeniti koordinate jedne tacke.
# Duz ima pocetnu i krajnju tacku, i duzinu (ne morate izracunavati duzinu na osnovu koordinata,
# nema potrebe). Pocetna i krajnja tacka, kao i duzina se mogu menjati.
# Cetvorougao ima 2 duzi, a i b. Mozemo mu izracunati obim (O = 2*a + 2*b, gde su a i b duzi koje
# opisuju cetvorougao, respektivno), i povrsinu (P = a * b, a i b su duzi koje opisuju cetvorougao).
from point import Point
from line import Line
from quadrilateral import Quadrilateral

if __name__ == '__main__':
    # defining 4 points
    point1 = Point(0, 0)
    point2 = Point(10, 10)
    point3 = Point(20, 10)
    point4 = Point(30, 50)
    point5 = Point(1, 5)
    # changing point coordinates
    point1.change_coordinates(100, 200)

    # defining 2 lines
    line_a = Line(point1, point2, 20)
    line_b = Line(point3, point4, 3)
    # changing point, a or b
    line_b.change_point_a(point5)
    # changing length of line
    line_b.change_length(130)

    # defining quadrilateral
    quad = Quadrilateral(line_a, line_b)
    # printing scope and surface
    print(f"Obim kvadrata je {quad.scope_of_quadrilateral()}cm.")
    print(f"Povrsina kvadrata je {quad.surface()}cm.")
