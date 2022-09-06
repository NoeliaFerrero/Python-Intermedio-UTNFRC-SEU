from operator import le


class Persona:
    def __init__ (self, dni, nombre):
        self.dni = dni
        self.nombre = nombre

    def __str__ (self):
        return f'DNI: {self.dni}, NOMBRE: {self.nombre}'

class Docente (Persona):
    def __init__ (self,dni,nombre,legajo,sueldo):
        super().__init__(dni,nombre)
        self.legajo = legajo
        self.sueldo = sueldo

    def __str__ (self):
        #str_docente = f'DNI: {self.dni}, NOMBRE: {self.nombre}, LEG: {self.legajo}, SUELDO: $ {self.sueldo}'
        #return str_docente
        str_persona = super().__str__()
        str_persona += f'\nLEG: {self.legajo}\nSUELDO: $ {self.sueldo}'
        return str_persona

class Alumno (Persona):
    def __init__ (self,dni,nombre,legajo,nota1,nota2):
        super().__init__(dni,nombre)
        self.legajo = legajo
        self.nota1 = nota1
        self.nota2 = nota2

    def __str__ (self):
        str_persona = super().__str__()
        str_persona += f'\nLEG. EST.: {self.legajo}'
        str_persona += f'\nNOTA 1: {self.nota1} - NOTA 2: {self.nota2}'
        return str_persona

class Curso:
    def __init__ (self,nombre,docente):
        self.nombre = nombre
        self.docente = docente
        self.alumnos = []

    def __str__ (self):
        str_curso = f'--- CURSO ---\nNOMBRE: {self.nombre}\n--- DOCENTE ---\n{self.docente}'
        return str_curso

    def listado_alumnos (self):
        str_alumnos = ''
        for alumno in self.alumnos:
            str_alumnos += f'\n{alumno.legajo} - {alumno.nombre} ({alumno.dni})'
        return str_alumnos

    def cantidad_regulares (self):
        cant = 0
        for alumno in self.alumnos:
            if alumno.nota1 >= 4 and alumno.nota2 >= 4:
                cant += 1
        return cant

    def promedio_total (self):
        cant = 0
        acum_notas = 0
        for alumno in self.alumnos:
            cant += 1
            acum_notas += alumno.nota1
            acum_notas += alumno.nota2
        if cant > 0:
            promedio = acum_notas/(cant*2)
        else:
            promedio = 0
        return promedio



def main ():
    docente = Docente('23684471','Martin Casatti','85005','100000')
    #print(docente)

    alumno1 = Alumno('21395678','Analia Guzman','35005',8,6)
    alumno2 = Alumno('22157887','Marcelo Guzman','35006',2,6)
    alumno3 = Alumno('15445887','Analia Gutierrez','35007',4,10)
    #print (alumno)

    curso = Curso('PYTHON INTERMEDIO',docente)
    curso.alumnos.append(alumno1)
    curso.alumnos.append(alumno2)
    curso.alumnos.append(alumno3)

    #print (curso)
    print (curso.listado_alumnos())

    print (f'El curso {curso.nombre} tiene {curso.cantidad_regulares()} alumnos regulares.')
    
    promedio = curso.promedio_total()
    if (promedio > 0):
        print (f'En el curso {curso.nombre} el promedio de notas de los alumnos es de {curso.promedio_total()}.')
    else:
        print (f'En el curso {curso.nombre}, NO HAY ALUMNOS INSCRIPTOS')
main()