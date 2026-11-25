class Equipo():
    def __init__(self, codigo, nombre, marca, unidades):
        self.codigo = codigo
        self.nombre = nombre
        self.marca = marca
        self.unidades = unidades

    def prestar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("Error: la cantidad debe ser mayor que cero.")
        if cantidad > self.unidades:
            raise ValueError(f"Error: solo hay {self.unidades} unidades.")
        self.unidades -= cantidad

    def __str__(self):
        return f"{self.codigo:<8}{self.nombre:<18}{self.marca:<14}{self.unidades:<8}"

class ListaEquipos:
    def __init__(self):
        self.listaEquipos = []
        self.cargar_datos()
    def cargar_datos(self):
        lista = [Equipo(1, "Multímetro", "Fluke", 10),
                 Equipo(2, "Osciloscopio", "Rigol", 4)]
        for i in lista:
            self.listaEquipos.append(i)
    def registrar(self, nombre, marca, unidades):
        if nombre.strip() == "" or marca.strip() == "":
            raise ValueError("Error: el nombre y la marca no pueden estar vacíos.")
        if unidades <= 0:
            raise ValueError("Error: las unidades no pueden ser menor o igual a cero.")
        codigo = len(self.listaEquipos) + 1
        self.listaEquipos.append(Equipo(codigo, nombre, marca, unidades))
        return codigo
    def buscar(self, codigo):
        for e in self.listaEquipos:
            if e.codigo == codigo:
                return e
        raise ValueError("Error: no existe ese código.")
    def prestar_equipos(self, codigo, cantidad):
        equipo = self.buscar(codigo)
        equipo.prestar(cantidad)
        return equipo.unidades
    def mostrar_equipos(self):
        return self.listaEquipos
    
