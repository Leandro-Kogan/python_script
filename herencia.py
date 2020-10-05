"""La herencia hace referencia a dos clases, una padre y la otra clase hija 
como por ejemplo podemos decir que hay una clase llamada persona, donde tenemos 
las caracteristicas pertenecientes a cualquier persona y luego tenemos una clase 
llamada empleado, donde se le adjudicaran atributos especificos pertenecientes
a un empleado, pero tambien tendra los atributos de la clase padre PERSONA """

class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    #Para imprimir los datos de un objeto creado a partir de una clase y que nos 
    #figuren los atributos y no la direccion de la memoria en la que se encuentra
    #usaremos __str__  que devuelve una cadena de texto:
    def __str__(self):
        return "Nombre "+ self.nombre+", edad "+str(self.edad)
        
    
    def saludo(self):
        print(f"Mi nombre es {self.nombre} y tengo {self.edad}")
#Al crear la clase empleado le especificamos que hereda las caracteristicas de 
#la clase PERSONA:        
class empleado(persona):
    def __init__(self, nombre, edad, sueldo):#Aqui hemos agregado tambien los atributos
#de la clase padre (persona) ya que al crearse un objeto de clase empleado 
#deberia tener tambien los atributos de la clase persona.
        super().__init__(nombre, edad)
        self.sueldo = sueldo
#"""Con super().__init__(nombre, edad) estamos haciendo referencia a los atributos 
#de la clase padre, luego con self definimos los atributos de la clase hija"""
    def datos(self):
        print(f"Nombre {self.nombre}, edad {self.edad}, salario {self.sueldo}")

    def __str__(self):
        return super().__str__()+ " salario "+ str(self.sueldo)

per1 = persona("Koko", 36)
per1.saludo()


print(per1)
empleado1 = empleado("Jorge", 49, 7000)
empleado1.datos()
print(empleado1)