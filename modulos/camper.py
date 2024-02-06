import json
from datetime import datetime

class Camper:
    def __init__(self, id, nombre, apellido, direccion, acudiente, telefono_celular, telefono_fijo, estado):
        self.N_Identificacion = id
        self.Nombre = nombre
        self.Apellido = apellido
        self.Direccion = direccion
        self.Acudiente = acudiente
        self.Telefono_Celular = telefono_celular
        self.Telefono_Fijo = telefono_fijo
        self.Estado = estado

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

campers_list = cargar_datos_desde_json("campers.json") or []

def menu():
    while True:
        print(""" 
  __  __ _____ _   _ _   _       ____   _    ____      _           ____    _    __  __ ____  _____ ____  ____  
 |  \/  | ____| \ | | | | |     |  _ \ / \  |  _ \    / \         / ___|  / \  |  \/  |  _ \| ____|  _ \/ ___| 
 | |\/| |  _| |  \| | | | |     | |_) / _ \ | |_) |  / _ \       | |     / _ \ | |\/| | |_) |  _| | |_) \___ \ 
 | |  | | |___| |\  | |_| |     |  __/ ___ \|  _ <  / ___ \      | |___ / ___ \| |  | |  __/| |___|  _ < ___) |
 |_|  |_|_____|_| \_|\___/      |_| /_/   \_\_| \_\/_/   \_\      \____/_/   \_\_|  |_|_|   |_____|_| \_\____/ 
                                                                                                               
 """)
        print("1. Registrar Datos")
        print("2. Ver Estado")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_datos_camper()
        elif opcion == "2":
            ver_estado_camper()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def registrar_datos_camper():
    id_camper = input("Ingrese su número de identificación: ")
    try:
        id_camper = int(id_camper)
    except ValueError:
        print("Número de identificación no válido. Intente de nuevo.")
        return

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    direccion = input("Ingrese su dirección: ")
    telefono_celular = input("Ingrese su número de teléfono celular: ")
    telefono_fijo = input("Ingrese su número de teléfono fijo: ")
    estado = "Inscrito"
    
    camper = Camper(id_camper, nombre, apellido, direccion, telefono_celular, telefono_fijo, estado)
    campers_list.append(camper.__dict__)
    guardar_datos_en_json("campers.json", campers_list)
    print("¡Datos registrados exitosamente!")

def ver_estado_camper():
    id_camper = input("Ingrese su número de identificación: ")
    try:
        id_camper = int(id_camper)
    except ValueError:
        print("Número de identificación no válido. Intente de nuevo.")
        return

    for camper in campers_list:
        if camper["N_Identificacion"] == id_camper:
            print("Estado actual:", camper["Estado"])
            break
    else:
        print("Camper no encontrado.")

menu()