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
































