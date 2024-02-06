import json
from datetime import datetime

class Entrenador:
    def __init__(self, id, nombre, rutas_asignadas, horario):
        self.N_Identificacion = id
        self.Nombre = nombre
        self.Rutas_Asignadas = rutas_asignadas
        self.Horario = horario

def cargar_datos_desde_json(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}

def guardar_datos_en_json(nombre_archivo, data):
    with open(nombre_archivo, 'w') as file:
        json.dump(data, file, indent=4)

def mostrar_info_entrenadores(entrenadores):
    if not entrenadores:
        print("No hay entrenadores registrados.")
    else:
        print("Información de todos los entrenadores:")
        for entrenador in entrenadores.values():
            print(f"ID: {entrenador.N_Identificacion}, Nombre: {entrenador.Nombre}, Rutas Asignadas: {entrenador.Rutas_Asignadas}, Horario: {entrenador.Horario}")
        print()

def agregar_entrenador(entrenadores):
    id_entrenador = input("Ingrese la identificación del nuevo entrenador: ")
    nombre_entrenador = input("Ingrese el nombre del nuevo entrenador: ")
    rutas_asignadas = input("Ingrese las rutas asignadas al nuevo entrenador (separadas por comas): ").split(',')
    horario_entrenador = input("Ingrese el horario del nuevo entrenador: ")

    nuevo_entrenador = Entrenador(id_entrenador, nombre_entrenador, rutas_asignadas, horario_entrenador)
    entrenadores[id_entrenador] = nuevo_entrenador

    print("Nuevo entrenador agregado exitosamente.")
    print()

def mostrar_menu():
    print("MENU:")
    print("1. Ver información de todos los entrenadores")
    print("2. Agregar un nuevo entrenador")
    print("3. Guardar cambios")
    print("4. Salir")

def main():
    nombre_archivo = "entrenadores.json"
    datos = cargar_datos_desde_json(nombre_archivo)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            mostrar_info_entrenadores(datos)
        elif opcion == "2":
            agregar_entrenador(datos)
        elif opcion == "3":
            guardar_datos_en_json(nombre_archivo, datos)
            print("Cambios guardados exitosamente.")
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()