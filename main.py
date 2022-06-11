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

# destruktor
class Test:
    def __del__(cls):
        print('bye class')


obj = Test()
lista = [obj]
del obj, lista[0]
print('end')
# destruktor wykonuje się, gdy nie mamy w programie żadnej referencji do klasy

print('\n')


# hermetyzacja (ukrywanie danych)
class Test2:
    lista = []

    def dodaj(self, arg):
        self.lista.append(arg)

    def usun(self):
        if len(self.lista) > 0:
            return self.lista.pop(-1)
        else:
            return


obj2 = Test2()
obj2.dodaj("A")
obj2.dodaj("B")
print(obj2.usun())
obj2.lista.append('X')
print(obj2.lista)

# publiczne - normalna nazwa, zastrzeżone - _, prywatne - __

print('\n')

# metody klas oraz statyczne
from random import randint


class Femoid:
    def __init__(self, imie):
        self.imie = imie

    def hejka(self):
        return f'Hejka, tu {self.imie}'

    @classmethod
    def nowy_femoid(cls, imie):
        return cls(imie)

    @staticmethod
    def humor():
        __lista_humorków = ['zły', 'dobry']
        __humorek = randint(0, 1)
        return f'{__class__.__name__} ma dziś {__lista_humorków[__humorek]} humor'


Ania = Femoid.nowy_femoid('Ania')
print(Ania.hejka())
Bombas = Ania.nowy_femoid('Bombas')
print(Bombas.hejka())
print(Femoid.humor())
print(Ania.humor())

# metody klasy do tworzenia nowych obiektów z nazwy klasy lub już powstałych, a metody statyczne do wywołania z nazwy klasy lub już powstałych obiektów
