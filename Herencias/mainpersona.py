from estudiante import Estudiante
from docente import Docente

estudiantes=[
    Estudiante("Daniela", "Corte","0150749950","0994641381","daniela.corte.est@tecazuay.edu.ec", 20,"cdla.jaime roldos","TSUDS", [8, 6.7,7.2,9,5]),
    Estudiante("Juan", "Perez","0165834424","0995654381","juan.perez.est@tecazuay.edu.ec", 16,"miraflores","Administracion de empresas", [6, 6,2,9.7,4.5,9]),
    Estudiante("Ariana", "Dominguez","0774728493","0948737467","ariana.domin.est@tecazuay.edu.ec", 18,"sinicay","Big Data", [5, 6.7,9.7,2,6.9]),
    Estudiante("Mateo", "Bermeo","0294848410","0998364663","mateo.bermeo.est@tecazuay.edu.ec", 17,"las peñas","entrenamiento deportivo", [9, 7.4,4.2,5.8,5]),
    Estudiante("Josue", "Pacho","01507453303","0976364481","josue.pacho.est@tecazuay.edu.ec", 24,"huaynacapac","TSUDS", [9,4.5,6.3,10,10])
]
docentes= [
    Docente("Luis","Tacuri","0424156723","0938746312","luis.tac@prof.edu.ec",30,"La floresta","POO",5),
    Docente("Olga","Arpi","0774664664","0955334332","olga.arpi@prof.edu.ec",45,"Mutualista Azuay","Web",8),
    Docente("Renata","Peralta","0263636363","0956563164","renata.peral@prof.edu.ec",25,"La floresta","Expresion Oral",2),
    Docente("Camila","Juarez","0424156723","0935654345","cami.juarez@prof.edu.ec",50,"Miraflores","Estadistica",9),
    Docente("John","Lopez","0424156723","0935456531","john.lop@prof.edu.ec",48,"La floresta","Base Datos",15)
]
print("ESTUDIANTE")
print(estudiantes.validar_edad())

print("DOCENTE")
print(docentes.calcular_salario())



