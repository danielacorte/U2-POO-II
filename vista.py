class VistaOperacion:
    def menu(self):
        print("\n" + "-" * 10, "MENÚ DE USUARIO", "-" * 10)
        print("1. Registrar equipo")
        print("2. Mostrar equipos")
        print("3. Prestar equipo")
        print("4. Salir")
        opcion = int(input("Ingrese una opción: "))
        return opcion

    def solicitar_datos(self):
        nombre = input("Ingrese el nombre del equipo: ")
        marca = input("Ingrese la marca: ")
        unidades = int(input("Ingrese las unidades: "))
        return nombre, marca, unidades

    def solicitar_codigo(self):
        return int(input("Ingrese el código del equipo: "))

    def solicitar_cantidad(self):
        return int(input("Ingrese la cantidad a prestar: "))

    def mostrar_equipos(self, equipos):
        print(f"{'Código':<8}{'Nombre':<18}{'Marca':<14}{'Unidades':<8}")
        print("-" * 48)
        for equipo in equipos:
            print(f"{equipo.codigo:<8}{equipo.nombre:<18}{equipo.marca:<14}{equipo.unidades:<8}")

    def mostrar_mensaje(self, mensaje):
        print(mensaje)