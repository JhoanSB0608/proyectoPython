import json

class Camper:
    def __init__(self, Nro_Identificacion, Nombre, Apellidos, Direccion, Acudiente, Telefono_Celular, Telefono_Fijo, Estado):
        self.Nro_Identificacion = Nro_Identificacion
        self.Nombre = Nombre
        self.Apellidos = Apellidos
        self.Direccion = Direccion
        self.Acudiente = Acudiente
        self.Telefono_Celular = Telefono_Celular
        self.Telefono_Fijo = Telefono_Fijo
        self.Estado = Estado

def registrar_camper():
    try:
        camper = {}
        camper["Nro_Identificacion"] = int(input("Ingrese el número de identificación del camper: "))
        camper["Nombre"] = input("Ingrese el nombre del camper: ")
        camper["Apellidos"] = input("Ingrese los apellidos del camper: ")
        camper["Direccion"] = input("Ingrese la dirección del camper: ")
        camper["Acudiente"] = input("Ingrese el nombre del acudiente del camper: ")
        camper["Telefono_Celular"] = input("Ingrese el número de teléfono celular del camper: ")
        camper["Telefono_Fijo"] = input("Ingrese el número de teléfono fijo del camper: ")
        camper["Estado"] = "Inscrito"  
        
        campers_list = cargar_datos_desde_json("campers.json")
        
        campers_list.append(camper)
        
        guardar_datos_en_json("campers.json", campers_list)
        
        print("Camper registrado exitosamente.")
    except ValueError:
        print("Error: Por favor ingrese un número válido para el número de identificación.")
    except Exception as e:
        print(f"Error al registrar el camper: {e}")

def cargar_datos_desde_json(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error al cargar datos desde JSON: {e}")
        return []

def guardar_datos_en_json(nombre_archivo, data):
    try:
        with open(nombre_archivo, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Datos guardados correctamente en el archivo {nombre_archivo}.")
    except Exception as e:
        print(f"Error al guardar los datos en el archivo {nombre_archivo}: {e}")

def menu():
    campers_list = cargar_datos_desde_json("campers.json")
    
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
            registrar_datos_camper(campers_list)
        elif opcion == "2":
            ver_estado_camper(campers_list)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def registrar_datos_camper(campers_list):
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
    estado = input("Ingrese el estado del camper: ")
    acudiente = input("Ingrese el nombre del acudiente: ")
    nuevo_camper = Camper(id_camper, nombre, apellido, direccion, acudiente, telefono_celular, telefono_fijo, estado)
    campers_list.append(nuevo_camper.__dict__)
    guardar_datos_en_json("campers.json", campers_list)
    print("¡Datos registrados exitosamente!")

def ver_estado_camper(campers_list):
    id_camper = input("Ingrese su número de identificación: ")
    try:
        id_camper = int(id_camper)
    except ValueError:
        print("Número de identificación no válido. Intente de nuevo.")
        return

    for camper in campers_list:
        if camper["Nro_Identificacion"] == id_camper:
            print("Estado actual:", camper["Estado"])
            break
    else:
        print("Camper no encontrado.")
        
if __name__ == "__main__":
    menu()