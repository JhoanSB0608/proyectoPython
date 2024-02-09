import os
import json

def load_rutas_json():
    try:
        with open(os.path.join("data", "rutas_entrenamiento.json"), 'r') as rutas_json:        
            lista_rutasEntrenamiento = json.load(rutas_json)
            print("La lista de rutas de entrenamiento ha sido cargada")
            return lista_rutasEntrenamiento
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return [] 

lista_rutasEntrenamiento = load_rutas_json()

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
        with open(os.path.join("data", "rutas_entrenamiento.json"), 'w') as rutas_json:
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
        print("\n--- Menú ---")
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