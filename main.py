from turtle import pos
from curso import Curso
# print("-------Clase default---------")
# print(Curso.nombre)
# print(Curso.creditos)
# print(Curso.duracion)
# print(Curso.area)

# prerequisito = Curso()
# print("----- Objeto prerrequisito sin asignar nada")
# print(prerequisito.nombre)
# print(prerequisito.creditos)
# print(prerequisito.duracion)
# print(prerequisito.area)

# print("------- Objeto prerequisito------------")
# prerequisito.nombre = "Mate computo 1"
# prerequisito.creditos = 5
# prerequisito.duracion = 50
# prerequisito.area = "Ciencias de la computacion"
# prerequisito.nota = 61

# print(prerequisito.nombre)
# print(prerequisito.creditos)
# print(prerequisito.duracion)
# print(prerequisito.area)

# postrequisito = Curso()
# print("--------Objeto Postrequisito--------")
# postrequisito.nombre = "Organizacion computacional"
# postrequisito.creditos = 3
# postrequisito.duracion = 100
# postrequisito.area = "Ciencias de la computacion"

# print(postrequisito.nombre)
# print(postrequisito.creditos)
# print(postrequisito.duracion)
# print(postrequisito.area)

# print("Notas de pre y post requisito")
# print("prerequisoto:")
# print(prerequisito.obtener_nota())
# print("postrequisoto:")
# print(postrequisito.obtener_nota())

print("-------Objeto prerequisito-------")
prerequisito = Curso("IPC1", 4, 100, "Desarrollo de software",0)
prerequisito.imprimir_atri()

print("-------Objeto postrequisito-------")
postrequisito = Curso("Estructura de Datos", 5, 100, "Desarrollo de software",0)
postrequisito.imprimir_atri()