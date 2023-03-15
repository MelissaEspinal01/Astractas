from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    @abstractmethod
    def Caminar(self):
        pass

class Trabajadores(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    
    def Caminar(self):
        print("{} está caminando hacia su trabajo.".format(self.nombre))

class Ingenieros(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    
    def Caminar(self):
        print("{} está construyendo un puente.".format(self.nombre))

class Licenciados(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
       
    def Caminar(self):
        print("{} está dando clase en la universidad.".format(self.nombre))
    
    def descripcion(self):
            print("{} es un licenciado {}.".format(self.nombre, "en la especialidad en matemáticas"))

perosna = Trabajadores("Raúl", 23)
ing= Ingenieros("Miguel", 30)
lic = Licenciados("Rafael", 36)

perosna.Caminar()
ing.Caminar()
lic.Caminar()

lic.descripcion()

