# Clase Electrodomestico
class Electrodomestico:
    # Constantes por defecto
    PRECIO_BASE_DEFECTO = 100
    COLOR_DEFECTO = "blanco"
    CONSUMO_ENERGETICO_DEFECTO = "F"
    PESO_DEFECTO = 5

    # Lista de colores válidos
    COLORES_DISPONIBLES = ["blanco", "negro", "rojo", "azul", "gris"]

    # Constructor
    def __init__(self, precio_base=PRECIO_BASE_DEFECTO, color=COLOR_DEFECTO, consumo_energetico=CONSUMO_ENERGETICO_DEFECTO, peso=PESO_DEFECTO):
        self.precio_base = precio_base
        self.color = self.__comprobarColor(color)
        self.consumo_energetico = self.__comprobarConsumoEnergetico(consumo_energetico)
        self.peso = peso

    # Métodos para comprobar si el color y el consumo energético son correctos
    def __comprobarConsumoEnergetico(self, letra):
        return letra.upper() if letra.upper() in ["A", "B", "C", "D", "E", "F"] else self.CONSUMO_ENERGETICO_DEFECTO

    def __comprobarColor(self, color):
        return color.lower() if color.lower() in self.COLORES_DISPONIBLES else self.COLOR_DEFECTO

    # Método para calcular el precio final en función del consumo energético y el peso
    def precioFinal(self):
        # Aumenta el precio según el consumo energético
        if self.consumo_energetico == "A":
            self.precio_base += 100
        elif self.consumo_energetico == "B":
            self.precio_base += 80
        elif self.consumo_energetico == "C":
            self.precio_base += 60
        elif self.consumo_energetico == "D":
            self.precio_base += 50
        elif self.consumo_energetico == "E":
            self.precio_base += 30
        elif self.consumo_energetico == "F":
            self.precio_base += 10

        # Aumenta el precio según el peso
        if 0 <= self.peso < 20:
            self.precio_base += 10
        elif 20 <= self.peso < 50:
            self.precio_base += 50
        elif 50 <= self.peso < 80:
            self.precio_base += 80
        elif self.peso >= 80:
            self.precio_base += 100

        return self.precio_base


# Clase Lavadora que hereda de Electrodomestico
class Lavadora(Electrodomestico):
    CARGA_DEFECTO = 5

    def __init__(self, precio_base=Electrodomestico.PRECIO_BASE_DEFECTO, color=Electrodomestico.COLOR_DEFECTO, consumo_energetico=Electrodomestico.CONSUMO_ENERGETICO_DEFECTO, peso=Electrodomestico.PESO_DEFECTO, carga=CARGA_DEFECTO):
        super().__init__(precio_base, color, consumo_energetico, peso)
        self.carga = carga

    # Método para calcular el precio final de la lavadora
    def precioFinal(self):
        precio_final = super().precioFinal()
        if self.carga > 30:
            precio_final += 50
        return precio_final

    # Método get para la carga
    def get_carga(self):
        return self.carga


# Clase Television que hereda de Electrodomestico
class Television(Electrodomestico):
    RESOLUCION_DEFECTO = 20
    SINTONIZADOR_DEFECTO = False

    def __init__(self, precio_base=Electrodomestico.PRECIO_BASE_DEFECTO, color=Electrodomestico.COLOR_DEFECTO, consumo_energetico=Electrodomestico.CONSUMO_ENERGETICO_DEFECTO, peso=Electrodomestico.PESO_DEFECTO, resolucion=RESOLUCION_DEFECTO, sintonizador=SINTONIZADOR_DEFECTO):
        super().__init__(precio_base, color, consumo_energetico, peso)
        self.resolucion = resolucion
        self.sintonizador = sintonizador

    # Método para calcular el precio final de la televisión
    def precioFinal(self):
        precio_final = super().precioFinal()
        if self.resolucion > 40:
            precio_final *= 1.3
        if self.sintonizador:
            precio_final += 50
        return precio_final

    # Métodos get para la resolución y el sintonizador TDT
    def get_resolucion(self):
        return self.resolucion

    def get_sintonizador(self):
        return self.sintonizador


# Clase Ejecutable
class Ejecutable:
    def main(self):
        # Crear un array de Electrodomésticos
        electrodomesticos = [
            Lavadora(200, "blanco", "A", 50, 40),
            Television(300, "negro", "B", 25, 50, True),
            Lavadora(150, "gris", "D", 30, 25),
            Television(400, "rojo", "C", 40, 30, False),
            Lavadora(180, "azul", "F", 60, 35),
            Television(250, "negro", "E", 10, 60, True),
            Electrodomestico(100, "blanco", "C", 45),
            Electrodomestico(200, "negro", "B", 20),
            Lavadora(160, "rojo", "D", 70, 50),
            Television(500, "azul", "A", 80, 50, True)
        ]

        total_precio_electrodomesticos = 0
        total_precio_lavadoras = 0
        total_precio_televisores = 0

        # Calcular el precio final de cada electrodoméstico y sumarlos
        for electrodomestico in electrodomesticos:
            precio = electrodomestico.precioFinal()
            total_precio_electrodomesticos += precio
            if isinstance(electrodomestico, Lavadora):
                total_precio_lavadoras += precio
            elif isinstance(electrodomestico, Television):
                total_precio_televisores += precio

        # Mostrar los precios
        print(f"Total precio de electrodomésticos: {total_precio_electrodomesticos} €")
        print(f"Total precio de lavadoras: {total_precio_lavadoras} €")
        print(f"Total precio de televisores: {total_precio_televisores} €")


# Ejecutar la clase ejecutable
if __name__ == "__main__":
    Ejecutable().main()
