from vehiculo import Vehiculo
from lista import  List

class FlotaVehiculos:
    def __init__(self):
        self.vehiculos = List()  # Usamos tu lista enlazada

    def registrar_vehiculo(self, placa, marca, modelo, año, kilometraje):
        nuevo_vehiculo = Vehiculo(placa, marca, modelo, año, kilometraje)
        self.vehiculos.append(nuevo_vehiculo)  # Usamos append de tu lista

    def eliminar_vehiculo(self, placa):
        actual = self.vehiculos.head
        prev = None
        while actual:
            if actual.value.placa == placa:
                if prev:
                    prev.next = actual.next
                else:
                    self.vehiculos.head = actual.next
                if actual == self.vehiculos.tail:
                    self.vehiculos.tail = prev
                self.vehiculos.size -= 1
                return
            prev = actual
            actual = actual.next
        raise ValueError("Vehículo no encontrado.")

    def buscar_vehiculo(self, placa):
        actual = self.vehiculos.head
        while actual:
            if actual.value.placa == placa:
                return actual.value
            actual = actual.next
        raise ValueError("Vehículo no encontrado.")

    def listar_vehiculos(self):
        if self.vehiculos.is_empty():
            print("No hay vehículos registrados.")
        else:
            print("Vehículos registrados:")
            self.vehiculos.show()