# ==========================================
# CLASE BASE: VEHICULO
# ==========================================

class Vehiculo:

    # Constructor de la clase
    def __init__(self, marca, modelo):

        try:

            # Validar que la marca no esté vacía
            if not marca:
                raise ValueError("La marca no puede estar vacía")

            # Validar que el modelo no esté vacío
            if not modelo:
                raise ValueError("El modelo no puede estar vacío")

            # Atributos del vehículo
            self.marca = marca
            self.modelo = modelo
            self.velocidad_actual = 0

        # Captura de errores
        except ValueError as error:

            print(f"Error en creación del vehículo: {error}")

    # Método para acelerar
    def acelerar(self, turbo=False, terreno="normal"):

        try:

            # Velocidad base
            incremento = 10

            # Validar tipo de dato del turbo
            if not isinstance(turbo, bool):
                raise TypeError("El parámetro turbo debe ser booleano")

            # Validar tipo de terreno
            if terreno not in ["normal", "difícil"]:
                raise ValueError("Terreno no válido")

            # Aumentar velocidad con turbo
            if turbo:
                incremento += 10

            # Reducir velocidad en terreno difícil
            if terreno == "difícil":
                incremento -= 5

            # Actualizar velocidad
            self.velocidad_actual += incremento

            # Mostrar resultado
            print(f"{self.marca} {self.modelo} acelera a "
                  f"{self.velocidad_actual} km/h")

        # Error por tipo de dato
        except TypeError as error:

            print(f"Error de tipo: {error}")

        # Error por valor incorrecto
        except ValueError as error:

            print(f"Error de valor: {error}")

        # Cualquier otro error
        except Exception as error:

            print(f"Error inesperado: {error}")

    # Método para detener el vehículo
    def detener(self):

        try:

            # Reiniciar velocidad
            self.velocidad_actual = 0

            print(f"{self.marca} {self.modelo} se ha detenido")

        except Exception as error:

            print(f"Error al detener vehículo: {error}")

    # Método para mostrar información
    def obtener_informacion(self):

        try:

            return (f"Vehículo: {self.marca} {self.modelo} "
                    f"- Velocidad: {self.velocidad_actual} km/h")

        except Exception as error:

            return f"Error obteniendo información: {error}"
        
        # ==========================================
# CLASE HIJA: CARRO
# ==========================================

class Carro(Vehiculo):

    # Constructor
    def __init__(self, marca, modelo, puertas):

        # Heredar atributos de Vehiculo
        super().__init__(marca, modelo)

        try:

            # Validar puertas
            if puertas <= 0:
                raise ValueError("El número de puertas debe ser mayor a 0")

            self.puertas = puertas

        except ValueError as error:

            print(f"Error en carro: {error}")

    # Método propio
    def tocar_bocina(self):

        try:

            print(f"{self.marca} {self.modelo} dice: ¡Piii Piii!")

        except Exception as error:

            print(f"Error al tocar bocina: {error}")
        # ==========================================
# PRUEBAS DEL PROGRAMA
# ==========================================

try:

    # Crear vehículo correctamente
    vehiculo1 = Vehiculo("Toyota", "Corolla")

    # Mostrar información
    print(vehiculo1.obtener_informacion())

    # Acelerar normalmente
    vehiculo1.acelerar()

    # Acelerar con turbo
    vehiculo1.acelerar(turbo=True)

    # Acelerar en terreno difícil
    vehiculo1.acelerar(terreno="difícil")

    # Detener vehículo
    vehiculo1.detener()

    # Mostrar información final
    print(vehiculo1.obtener_informacion())

except Exception as error:

    print(f"Error general: {error}")


# ==========================================
# PRUEBAS DE ERRORES
# ==========================================

print("\n--- PRUEBAS DE EXCEPCIONES ---")

# Marca vacía
vehiculo2 = Vehiculo("", "Mazda")

# Modelo vacío
vehiculo3 = Vehiculo("Chevrolet", "")

# Turbo incorrecto
vehiculo1.acelerar(turbo="si")

# Terreno incorrecto
vehiculo1.acelerar(terreno="montaña")

# ==========================================
# CLASE HIJA: CARRO
# ==========================================

class Carro(Vehiculo):

    # Constructor
    def __init__(self, marca, modelo, puertas):

        # Heredar atributos de Vehiculo
        super().__init__(marca, modelo)

        try:

            # Validar puertas
            if puertas <= 0:
                raise ValueError("El número de puertas debe ser mayor a 0")

            self.puertas = puertas

        except ValueError as error:

            print(f"Error en carro: {error}")

    # Método propio
    def tocar_bocina(self):

        try:

            print(f"{self.marca} {self.modelo} dice: ¡Piii Piii!")

        except Exception as error:

            print(f"Error al tocar bocina: {error}")
            
            # ==========================================
# PRUEBA CLASE CARRO
# ==========================================

print("\n--- PRUEBA CLASE CARRO ---")

carro1 = Carro("Mazda", "CX-5", 4)

print(carro1.obtener_informacion())

carro1.tocar_bocina()

carro1.acelerar(turbo=True)

# Error de puertas
carro2 = Carro("Kia", "Picanto", 0)

#===========================================
# FIN DEL PROGRAMA 
#===========================================