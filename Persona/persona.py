import random

class Persona:
    # Constantes para el cálculo del IMC
    PESO_IDEAL = 0
    POR_DEBAJO = -1
    SOBREPESO = 1
    
    def __init__(self, nombre='', edad=0, sexo='H', peso=0.0, altura=0.0):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = self.__comprobar_sexo(sexo)
        self.__peso = peso
        self.__altura = altura
        self.__dni = self.__genera_dni()
    
    # Constructor solo con nombre, edad y sexo
    @classmethod
    def con_nombre_edad_sexo(cls, nombre, edad, sexo):
        return cls(nombre, edad, sexo)
    
    # Constructor por defecto
    @classmethod
    def por_defecto(cls):
        return cls()
    
    # Métodos privados
    def __comprobar_sexo(self, sexo):
        return sexo if sexo in ['H', 'M'] else 'H'
    
    def __genera_dni(self):
        numero = random.randint(10000000, 99999999)
        letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
        letra = letras[numero % 23]
        return f"{numero}{letra}"
    
    # Métodos públicos
    def calcularIMC(self):
        if self.__altura > 0:
            imc = self.__peso / (self.__altura ** 2)
            if imc < 20:
                return Persona.POR_DEBAJO
            elif 20 <= imc <= 25:
                return Persona.PESO_IDEAL
            else:
                return Persona.SOBREPESO
        return None
    
    def esMayorDeEdad(self):
        return self.__edad >= 18
    
    def toString(self):
        return (f"Nombre: {self.__nombre}, Edad: {self.__edad}, Sexo: {self.__sexo}, "
                f"Peso: {self.__peso} kg, Altura: {self.__altura} m, DNI: {self.__dni}")
    
    # Métodos set
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def setEdad(self, edad):
        self.__edad = edad
    
    def setSexo(self, sexo):
        self.__sexo = self.__comprobar_sexo(sexo)
    
    def setPeso(self, peso):
        self.__peso = peso
    
    def setAltura(self, altura):
        self.__altura = altura


# Función para pedir datos por teclado
def pedir_datos():
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))
    sexo = input("Introduce el sexo (H/M): ")
    peso = float(input("Introduce el peso (kg): "))
    altura = float(input("Introduce la altura (m): "))
    return nombre, edad, sexo, peso, altura


# Crear tres objetos según los requisitos
print("Datos para el primer objeto:")
nombre, edad, sexo, peso, altura = pedir_datos()
persona1 = Persona(nombre, edad, sexo, peso, altura)

print("\nDatos para el segundo objeto:")
nombre, edad, sexo, _, _ = pedir_datos()
persona2 = Persona.con_nombre_edad_sexo(nombre, edad, sexo)

print("\nCreando el tercer objeto por defecto:")
persona3 = Persona.por_defecto()

# Usar los métodos set para asignar valores al tercer objeto
persona3.setNombre("Carlos")
persona3.setEdad(30)
persona3.setSexo("H")
persona3.setPeso(85)
persona3.setAltura(1.75)

# Función para mostrar el estado de peso
def mostrar_peso_ideal(persona):
    imc_resultado = persona.calcularIMC()
    if imc_resultado == Persona.POR_DEBAJO:
        print(f"{persona.toString()} está por debajo de su peso ideal.")
    elif imc_resultado == Persona.PESO_IDEAL:
        print(f"{persona.toString()} está en su peso ideal.")
    elif imc_resultado == Persona.SOBREPESO:
        print(f"{persona.toString()} tiene sobrepeso.")
    else:
        print(f"No se puede calcular el IMC para {persona.toString()}")

# Comprobación del peso ideal y si son mayores de edad
for persona in [persona1, persona2, persona3]:
    mostrar_peso_ideal(persona)
    print(f"¿Es mayor de edad? {'Sí' if persona.esMayorDeEdad() else 'No'}")
    print("\n")

