from modelo import*
from vista import VistaOperacion
from controlador import ControladorEquipo

modelo= ListaEquipos()
vista=VistaOperacion()
controlador=ControladorEquipo(modelo,vista)
controlador.ejecutar()