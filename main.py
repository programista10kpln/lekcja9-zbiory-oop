# set - zbiór i operacje na zbiorach
liczby1 = {0, 1, 2, 4}
slowa = {1, 2, 6, 7, 8}
print(liczby1)
print(slowa)

liczby1.add(5)
print(liczby1)

liczby1.remove(0)
print(liczby1 | slowa)
print(liczby1 & slowa)
print(liczby1 - slowa)
print(liczby1 ^ slowa)


# klasy
class Czlowiek:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def przedstaw_sie(self):
        return 'Jestem ' + self.imie + ', mam ' + str(self.wiek) + ' lat'


obiekt1 = Czlowiek('Jakub', 19)  # tworzenie obiektu na podstawie klasy (szablonu)
print(obiekt1.przedstaw_sie())


# dziedziczenie
class Owad:
    def __init__(self, wielkosc, poziom_irytacji):
        self.wielkosc = wielkosc
        self.poziom_irytacji = poziom_irytacji


class Mucha(Owad):
    def odgłos(self):
        return f'To {self.wielkosc} {self.__class__.__name__} i robi bzzzzzzzzzzzzzzzz'  # koks string z zmiennymi


class Komar(Owad):
    def odgłos(self):
        return f'To {self.wielkosc} {self.__class__.__name__} i robi siorp siorp'  # koks string z zmiennymi


mucha = Mucha('średnia', 'mały')
print(mucha.odgłos())

komar = Komar('malutki', 'ogromny')
print(komar.odgłos())
print(komar.poziom_irytacji)

# magiczne metody to te z podłogami(__) i pokolorowane na różowo
