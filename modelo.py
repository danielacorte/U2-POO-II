class Equipo():
    def __init__(self, codigo, nombre, marca,unidades):
        self.codigo= codigo
        self.nombre= nombre
        self.marca=marca
        self.unidades=unidades

    def prestar(self,cantidad,unidades):
        if cantidad<=0 or cantidad > unidades:
            print("Error")
        else: 
            resta= cantidad-unidades
        return True
  
    def __str__(self):
        return

class ListaEquipos:
    def __init__(self):
        self.listaEquipos=[]
        self.cargar_datos()
    def cargar_datos(self):
        lista=[Equipo(1,"Multimetro", "Fluke",10),
               Equipo(2, "Osciloscopio", "Rigol", 4),]
        for i in lista:
            self.listaEquipos.append(i)
    def registrarLibro(self,codigo, nombre, marca, unidades):
        self.listaEquipos.append(Equipo(codigo, nombre, marca, unidades))
        return print("Equipo registrado correctamente")
    def prestar_equipos(self, codigo, unidades):
        for e in self.listaEquipos:
            if Equipo.codigo==codigo:
                return Equipo.prestar(unidades)
        return None
    def mostrar_equipos(self):
        return self.listaEquipos
    
