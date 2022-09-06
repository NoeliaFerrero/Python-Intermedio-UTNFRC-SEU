class Persona:

    def __init__ (self,nombre,edad,altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def __str__ (self):
        return f"Me llamo {self.nombre}, tengo {self.edad} años y mido {self.altura} m."

    def saludo (self):
        return f"Hola! Me llamo {self.nombre}"

    def esMayorEdad (self):
        return (self.edad >= 18)

    def cuantoPelo (self):
        # Hasta 40 mucho, entre 40 y 60 poco, más de 60 nada
        if (self.edad <= 40):
            return "MUCHO"
        elif (40 < self.edad <= 60):
            return "POCO"
        else:
            return "NADA"

'''
persona1 = Persona("Martin Casatti",48,1.75)
persona2 = Persona("Pepito",12,1.26)

print (persona1)
print (persona2)

print (persona1.esMayorEdad())
print (persona2.esMayorEdad())

print (persona2.saludo())

print (f"{persona1.nombre} que tiene {persona1.edad} tiene {persona1.cuantoPelo()} pelo.")
print (f"{persona2.nombre} que tiene {persona2.edad} tiene {persona2.cuantoPelo()} pelo.")
'''