
class Alumno:
    
    def __init__(self, nombre, apellido, legajo, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.dni = dni

    def __repr__(self):
        return f'Alumno <{self.apellido}, {self.nombre}>'


    def agregarAlumno(self):
        pass
    
    def inscribirse(self, curso):
        curso.alumnos.append(self)
         
    # def cursar(self):
    #    raise NotImplementedError 
    #

class Materias: 
    
    def __init__(self, nombre, id, dia, profesor):
        self.nombre = nombre
        self.id = id
        self.dia = dia
        self.profesor = profesor

class Universidad:
    
    def __init__(self, nombre, carrera, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad

        self.carrera = carrera

        #self.listaAlumnos ={}
        #self.listaMaterias = {}
        #self.listaCursos = {}

    def profesor(self):
        pass

class Curso:

    def __init__(self, Materias, Alumno, anio):
        self.anio = anio
        self.materia = Materias
        self.alumnos = Alumno

    def inscribir(self, alumno):
        self.alumnos.append(alumno)


        # inscribir al alumno curso.inscribir(alumno)
        
if __name__ == " __main__":

    #creamos un par de materias
    edd = Materias(id=1, nombre="Esctructura", dia="Lunes", profesor="Santoro")
    par = Materias(id=2, nombre="Paradigma", dia="Viernes", profesor="Colombo")

    #creamos la carrera en un diccionario
    carrera = {
    "analisis":[edd, par]
    }

    #creamos una universidad
    ifts = Universidad(nombre="IFTS", ciudad="Palermo", carrera=carrera)

    #creamos algunos alumnos
    juan = Alumno("Juan", "Perez", 1, 1)
    jose = Alumno("Jose", "Duarte", 2, 2)
    martin = Alumno("Martin", "Dolina", 3, 3)

    #creamos un curso para tener de prueba
    curso_2018 = Curso(Materias=par, Alumno=[juan], anio=2018)

    jose.inscribirse(curso_2018)
    curso_2018.inscribir(martin)

    print(f"Alumnos: {curso_2018.alumnos}")
    print(curso_2018.alumnos)
    print("hola")