# obj_Computador.py
class Computador:
    def __init__(self, id_, marca, modelo):
        self._id = id_
        self._marca = marca
        self._modelo = modelo

    @property
    def id(self):
        return self._id

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    def __str__(self):
        return f"Computador(id={self._id}, marca={self._marca}, modelo={self._modelo})"
