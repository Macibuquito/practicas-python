# Practica 2
# print("Hola, esta es la práctica 2 en GitHub con Carlitos ❤️")

# Los cuatro pilares fundamentales de la POO:
   # aplicando los principios de:
       # 1. Abstracción  --> Solo muestras detalles escensiales de un objeto OCULTA complejidad interna
           # Basta con saber como acelerar, frenar y encender el coche, NO conocer su funcionamiento interno

print("Ej. Abstracción")
class Cafetera:
    def encender(self):
        print("Cafetera encendida")

    def preparar_cafe(self):
        print("Preparando cafe")

    def apagar(self):
        print("Cafetera apagada")

cafetera = Cafetera()
cafetera.preparar_cafe()


       # 2. Encapsulamiento  --> Ocultar datos internos, protege estado del objeto.
       # _atributo:  atributo protegido
       # __atributo: nombre manipulado (name mangling), atributo super protegido
       # Tambien se pueden encapsular los metodos, con _ o con __

print("Ej. Encapsulamiento")
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo # encapsulamiento

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad

    def obtener_saldo(self):
        return self._saldo

cuenta = CuentaBancaria("Juan", 1200)
print(cuenta.obtener_saldo())
cuenta.depositar(500)
print(cuenta.obtener_saldo())
print(cuenta._saldo)
print(cuenta.titular)



       # 3. Herencia  --> Una clase puede heredar ATRIBUTOS y METODOS de otras CLASE
          # Esto permite la reutilización del codigo :)


print("Ej. Herencia")
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("El animal hace un sonido")

class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre} dice ¡Guau!")

class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice !Miaw¡")

class Cangrejo(Animal):
    pass

p = Perro("Fido")
p.hablar()

g = Gato("Michisin")
g.hablar()

cg = Cangrejo("Don Cangrejo")
cg.hablar()








