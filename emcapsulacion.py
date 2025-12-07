class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre   
        self.__edad = edad       

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

persona = Persona("Ana", 20)
print(persona.get_nombre())

persona.set_nombre("María")
print(persona.get_nombre())
