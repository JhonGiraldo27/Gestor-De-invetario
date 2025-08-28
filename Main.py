
from metodos_registro import registrar_computador

def menu():
    while True:
        
        print("\n=== Menú Principal ===")
        print("1. Agregar computador")
        print("0. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            registrar_computador()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
