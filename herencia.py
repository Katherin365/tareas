class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        return "Hace un sonido"

class Perro(Animal):
    def sonido(self):
        return "Guau guau"

mi_perro = Perro("Firulais")
print(mi_perro.nombre, "dice:", mi_perro.sonido())
