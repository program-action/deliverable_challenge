import random

class Password:
    MAYUSCULAS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    MINUSCULAS = list("abcdefghijklmnopqrstuvwxyz")
    NUMEROS = list("0123456789")
    SIMBOLOS = list("!@#$%^&*-_=+;:,.<>?/")

    def __init__(self, longitud=8):
        self.__longitud = longitud
        self.__contrasena = self.generarPassword()

    def generarPassword(self):
        caracteres = Password.MAYUSCULAS + Password.MINUSCULAS + Password.NUMEROS + Password.SIMBOLOS
        return ''.join(random.choice(caracteres) for _ in range(self.__longitud))

    def esFuerte(self):
        mayusculas = sum(1 for char in self.__contrasena if char in Password.MAYUSCULAS)
        minusculas = sum(1 for char in self.__contrasena if char in Password.MINUSCULAS)
        numeros = sum(1 for char in self.__contrasena if char in Password.NUMEROS)
        simbolos = sum(1 for char in self.__contrasena if char in Password.SIMBOLOS)
        
        # Fortalezas de la contraseña
        condiciones = {
            "mayusculas": mayusculas >= 1,
            "minusculas": minusculas >= 1,
            "numeros": numeros >= 1,
            "simbolos": simbolos >= 1,
        }
        return condiciones

    def getContrasena(self):
        return self.__contrasena

    def getLongitud(self):
        return self.__longitud

    def setLongitud(self, longitud):
        self.__longitud = longitud
        self.__contrasena = self.generarPassword()

if __name__ == "__main__":
    while True:
        try:
            cantidad_passwords = int(input("¿Cuántas contraseñas quieres generar?: "))
            break  # Permitir cualquier cantidad sin restricciones
        except ValueError as e:
            print("Por favor, introduce un número válido.")

    while True:
        try:
            longitud_password = int(input("¿Cuál será la longitud de las contraseñas? (mínimo 8): "))
            if longitud_password < 8:
                raise ValueError("La longitud debe ser al menos 8.")
            break
        except ValueError as e:
            print(e)

    passwords = [Password(longitud_password) for _ in range(cantidad_passwords)]
    son_fuertes = [password.esFuerte() for password in passwords]

    print("\nContraseñas generadas:")
    for i in range(cantidad_passwords):
        fortaleza = son_fuertes[i]
        estado = "Fuerte" if all(fortaleza.values()) else "Débil"
        detalles = ', '.join([f"{k}: {'Sí' if v else 'No'}" for k, v in fortaleza.items()])
        print(f"{i + 1}. {passwords[i].getContrasena()} - {estado} (Detalles: {detalles})")
