from obj_Computador import Computador

_COMPUTADORES = []

def _es_id_unico(id_):
    return all(c.id != id_ for c in _COMPUTADORES)

def registrar_computador():
    print("\n=== Registrar Computador ===")
    id_ = input("ID: ").strip()
    if not id_:
        print("ID no puede estar vacío.")
        return None
    if not _es_id_unico(id_):
        print("Ese ID ya existe.")
        return None

    marca = input("Marca: ").strip()
    if not marca:
        print("Marca no puede estar vacía.")
        return None

    modelo = input("Modelo: ").strip()
    if not modelo:
        print("Modelo no puede estar vacío.")
        return None

    comp = Computador(id_, marca, modelo)
    _COMPUTADORES.append(comp)
    print("Registro exitoso:", comp)
    return comp
