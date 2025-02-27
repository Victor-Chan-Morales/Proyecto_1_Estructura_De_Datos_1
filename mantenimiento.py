class Mantenimiento:
    def __init__(self, fecha, descripcion, costo):
        self.fecha = fecha
        self.descripcion = descripcion
        self.costo = costo

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        if not isinstance(valor, str) or len(valor) != 10 or valor[4] != '-' or valor[7] != '-':
            raise ValueError("Formato de fecha inválido. Use YYYY-MM-DD.")
        self._fecha = valor

    @property
    def costo(self):
        return self._costo

    @costo.setter
    def costo(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("El costo debe ser mayor a cero")
        self._costo = valor

    def __str__(self):
        return f"Fecha: {self.fecha}, Descripción: {self.descripcion}, Costo: {self.costo}"