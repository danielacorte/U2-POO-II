class ControladorEquipo:
    def __init__(self, modelo, vista):
        self.modelo=modelo
        self.vista=vista
    def ejecutar(self):
        opcion = 0
        while opcion != 4:
            opcion=self.vista.menu()
            if opcion==1:
                try:
                    nombre, marca, unidades=self.vista.solicitar_datos()
                    mensaje=self.modelo.registrar(nombre, marca, unidades)
                    self.vista.mostrar_mensaje(mensaje)
                except ValueError:
                    self.vista.error("Datos ingresados incorrectamente")
            elif opcion==2:
                try:
                   self.vista.mostrar_equipos(self.modelo.mostrar_equipos()) 
                except ValueError:
                    self.vista.error("Lista vacia")
            elif opcion==3:
                try:
                    codigo, cantidad= self.vista.solicitar_codigo(),self.vista.solicitar_cantidad()
                    resta=self.modelo.prestar_equipos(codigo,cantidad)
                    if resta==True:
                       self.vista.mostrar_mensaje("Operacion realizada correctamente")
                    else:
                        self.vista.mostrar_mensaje("No hay unidades disponibles")
                except ValueError:
                    self.vista.error("Datos ingresados incorrrectamente")
            elif opcion==4:
                self.vista.mostrar_mensaje("Saliendo del programa...")
            else:
                self.vista.mostrar_mensaje("opcion invalida")
                

                
            

        
            