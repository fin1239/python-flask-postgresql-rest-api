from utils.DateFormant import DateFormat


class Movie():
    
    def __init__(self, ci, nombre=None, apellido=None, procedencia=None, fechaNac=None) ->None:
        self.ci = ci
        self.nombre = nombre
        self.appellido = apellido
        self.procedencia = procedencia
        self.fechaNac = fechaNac
        
    def to_JSON(self):
        return {
            'ci': self.ci,
            'nombre': self.nombre,
            'apellido': self.appellido,
            'procedencia': self.procedencia,
            'fechaNac': DateFormat.convert_date(self.fechaNac),
        }