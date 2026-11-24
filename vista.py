class VistaPperacion:
    def menu(self):
        print("-"*10,"MENU DE USUARIO","-"*10)
        print("1. Registar Equipo")
        print("2. Mostrar Equipos")
        print("3. Prestar Equipo")
        print("4. Salir")
        op=int(input("Ingrese una opcion: "))
        return op
    def solicitar_datos(self):
        nombre=input("Ingrese el nombre del libro: ")
        marca=input("Ingrese la marca del libro: ")
        unidades=int(input("Ingrese las unidades: "))
        return nombre,marca,unidades