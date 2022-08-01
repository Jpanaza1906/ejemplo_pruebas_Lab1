class Curso:
    def __init__(self, nombre, creditos, duracion, area, nota):
        self.nombre = nombre
        self.creditos = creditos
        self.duracion = duracion
        self.area = area
        self.nota = nota
        
    def obtener_nota(self):
        return self.nota
    def imprimir_atri(self):
        print(self.nombre)
        print(self.creditos)
        print(self.duracion)
        print(self.area)
        print(self.nota)