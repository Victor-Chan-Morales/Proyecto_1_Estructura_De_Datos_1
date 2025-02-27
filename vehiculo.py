from Proyecto_1_Estructura_De_Datos_1.mantenimiento import Mantenimiento
from lista import List
import re

class Vehiculo:
    def __init__(self, placa, marca, modelo, anio, kilometraje):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje
        self.historial_mantenimientos = List()

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, valor):
        if not isinstance(valor, int) or valor < 1900 or valor > 2025:
            raise ValueError("El año del vehículo debe estar entre 1900 y 2025")
        self._anio = valor

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, valor):
        formato_placa = r"^[PMC]\d{3}[A-Z]{3}$"
        valor_mayusculas = valor.upper()

        if not re.match(formato_placa, valor_mayusculas):
            raise ValueError("Formato de placa inválido. Debe ser P, M o C seguido de 3 dígitos y 3 letras.")

        self._placa = valor_mayusculas

    @property
    def kilometraje(self):
        return self._kilometraje

    @kilometraje.setter
    def kilometraje(self, valor):
        try:
            valor_entero = int(valor)
        except ValueError:
            raise ValueError("El kilometraje debe ser un número entero o una cadena que se pueda convertir a entero.")

        if valor_entero < 0:
            raise ValueError("El kilometraje debe ser un número mayor o igual a cero.")

        self._kilometraje = valor_entero

    def agregar_mantenimiento(self, fecha, descripcion, costo):
        mantenimiento = Mantenimiento(fecha, descripcion, costo)
        self.historial_mantenimientos.append(mantenimiento)

    def eliminar_mantenimiento(self, fecha):
        actual = self.historial_mantenimientos.head
        prev = None
        while actual:
            if actual.value.fecha == fecha:
                if prev:
                    prev.next = actual.next
                else:
                    self.historial_mantenimientos.head = actual.next
                if actual == self.historial_mantenimientos.tail:
                    self.historial_mantenimientos.tail = prev
                self.historial_mantenimientos.size -= 1
                return
            prev = actual
            actual = actual.next
        raise ValueError("Mantenimiento No Encontrado.")

    def mostrar_historial(self):
        if self.historial_mantenimientos.is_empty():
            print("No hay mantenimientos registrados actualmente.")
        else:
            print("Historial de mantenimientos:")
            self.historial_mantenimientos.show()

    def costo_total_mantenimientos(self):
        total = 0
        actual = self.historial_mantenimientos.head
        while actual:
            total += actual.value.costo
            actual = actual.next
        return total

    def __str__(self):
        return f"{self.marca} {self.modelo}, Año: {self.anio}, Kilometraje: {self.kilometraje}, Placa: {self.placa}"