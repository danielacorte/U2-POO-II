class Equipo:
    def __init__(self, codigo, nombre, marca, unidades):
        self.codigo = codigo
        self.nombre = nombre
        self.marca = marca
        self.unidades = unidades

    def prestar(self, cantidad):
        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor que cero.")
            return False
        if cantidad > self.unidades:
            print(f"Error: solo hay {self.unidades} unidades.")
            return False
        self.unidades -= cantidad
        return True

    def __str__(self):
        return f"{self.codigo:<8}{self.nombre:<18}{self.marca:<14}{self.unidades:<8}"


# Datos iniciales (dos objetos creados en el programa)
equipos = [
    Equipo(1, "Multímetro", "Fluke", 10),
    Equipo(2, "Osciloscopio", "Rigol", 4),
]


def leer_entero(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        return None


def registrar_equipo():
    nombre = input("Ingrese el nombre del equipo: ")
    marca = input("Ingrese la marca: ")
    unidades = leer_entero("Ingrese las unidades: ")
    if unidades is None or unidades < 0:
        print("Error: unidades no válidas.")
        return
    codigo = len(equipos) + 1
    equipos.append(Equipo(codigo, nombre, marca, unidades))
    print(f"Registrado con el código {codigo}.")


def mostrar_equipos():
    print(f"{'Código':<8}{'Nombre':<18}{'Marca':<14}{'Unidades':<8}")
    print("-" * 48)
    for equipo in equipos:
        print(equipo)


def prestar_equipo():
    codigo = leer_entero("Ingrese el código del equipo: ")
    encontrado = None
    for equipo in equipos:
        if equipo.codigo == codigo:
            encontrado = equipo
            break

    if encontrado is None:
        print("Error: no existe ese código.")
        return

    cantidad = leer_entero("Ingrese la cantidad a prestar: ")
    if cantidad is None:
        print("Error: cantidad no válida.")
        return

    if encontrado.prestar(cantidad):
        print(f"Listo. Quedan {encontrado.unidades} unidades.")


def menu():
    opcion = 0
    while opcion != 4:
        print("\n" + "-" * 10, "MENÚ DE USUARIO", "-" * 10)
        print("1. Registrar equipo")
        print("2. Mostrar equipos")
        print("3. Prestar equipo")
        print("4. Salir")
        opcion = leer_entero("Ingrese una opción: ")

        if opcion == 1:
            registrar_equipo()
        elif opcion == 2:
            mostrar_equipos()
        elif opcion == 3:
            prestar_equipo()
        elif opcion == 4:
            print("Hasta luego.")
        else:
            print("Opción no válida")


menu()
 
