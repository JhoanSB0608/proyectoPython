import os
import json

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

def load_rutas_json():
    return cargar_datos_desde_json(os.path.join("data/rutas_entrenamiento.json"))

def rutas_entrenamiento(lista_rutasEntrenamiento):
    
    ruta_nodejs = {
        "nombre": "NodeJS",
        "fundamentos": ["Introducción a la algoritmia", "PSeInt", "Python"],
        "programacion_web": ["HTML", "CSS", "Bootstrap"],
        "programacion_formal": ["JavaScript"],
        "bases_datos": ["MongoDb", "Postgresql"],
        "backend": ["NodeJS", "Express"]
    }

    ruta_java = {
        "nombre": "Java",
        "fundamentos": ["Introducción a la algoritmia", "PSeInt", "Python"],
        "programacion_web": ["HTML", "CSS", "Bootstrap", "JavaScript"],
        "programacion_formal": ["Java"],
        "bases_datos": ["Mysql", "MongoDb"],
        "backend": ["Spring Boot"]
    }

    ruta_netcore = {
        "nombre": "NetCore",
        "fundamentos": ["Introducción a la algoritmia", "PSeInt", "Python"],
        "programacion_web": ["HTML", "CSS", "JavaScript"],
        "programacion_formal": ["C#"],
        "bases_datos": ["Mysql", "MongoDb", "Postgresql"],
        "backend": ["NetCore"]
    }

    lista_rutasEntrenamiento.append(ruta_nodejs)
    lista_rutasEntrenamiento.append(ruta_java)
    lista_rutasEntrenamiento.append(ruta_netcore)
    
    guardar_json_rutas(lista_rutasEntrenamiento)
    listar_rutas(lista_rutasEntrenamiento)


def guardar_json_rutas(lista_rutasEntrenamiento):
    try:
        with open(os.path.join("data", "data/rutas_entrenamiento.json"), 'w') as rutas_json:
            json.dump(lista_rutasEntrenamiento, rutas_json, indent=2)
            print("La lista de rutas de entrenamiento ha sido guardada") 
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya rutas de entrenamiento guardadas.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido: {e}")


def listar_rutas(lista_rutasEntrenamiento):
    print("Listado de las rutas de entrenamiento: ")
    for ruta in lista_rutasEntrenamiento:
        print(ruta)

def menu():
    lista_rutasEntrenamiento = load_rutas_json()

    while True:
        print(""" 
  ____  _   _ _____  _    ____        ____  _____       _____ _   _ _____ ____  _____ _   _    _    __  __ ___ _____ _   _ _____ ___  
 |  _ \| | | |_   _|/ \  / ___|      |  _ \| ____|     | ____| \ | |_   _|  _ \| ____| \ | |  / \  |  \/  |_ _| ____| \ | |_   _/ _ \ 
 | |_) | | | | | | / _ \ \___ \      | | | |  _|       |  _| |  \| | | | | |_) |  _| |  \| | / _ \ | |\/| || ||  _| |  \| | | || | | |
 |  _ <| |_| | | |/ ___ \ ___) |     | |_| | |___      | |___| |\  | | | |  _ <| |___| |\  |/ ___ \| |  | || || |___| |\  | | || |_| |
 |_| \_\\___/  |_/_/   \_\____/      |____/|_____|     |_____|_| \_| |_| |_| \_\_____|_| \_/_/   \_\_|  |_|___|_____|_| \_| |_| \___/ 
                                                                                                                                      
""")
        print("1. Listar rutas de entrenamiento")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_rutas(lista_rutasEntrenamiento)
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()