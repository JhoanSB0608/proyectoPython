import json

def cargar_datos(archivo):
    try:
        with open(archivo, 'r') as f:
            datos = json.load(f)
        print(f"Los datos del archivo {archivo} han sido cargados")
        return datos
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe.")
        return [] 
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {archivo}. El formato podría ser incorrecto.")
        return []  
    except Exception as e:
        print(f"Error desconocido al cargar el archivo {archivo}: {e}")
        return []  

def guardar_datos(nombre_archivo, data):
    try:
        with open(nombre_archivo, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Los datos han sido guardados en el archivo {nombre_archivo}")
    except Exception as e:
        print(f"Error al guardar los datos en el archivo {nombre_archivo}: {e}")

def verificar_ruta_entrenamiento(ruta, lista_aulas):
    for aula in lista_aulas:
        ruta_asignada = aula.get('Ruta_Asignada')
        if ruta_asignada and ruta.lower() == ruta_asignada.lower():
            return True
    return False

def listar_aulas(lista_aulas):
    print("Listado de aulas de entrenamiento: ")
    for aula in lista_aulas:
        print(aula)

def menu_aula():
    lista_aulas = cargar_datos("data/salasEntreno.json")

    while True:
        print(""" 
     _   _   _ _        _    ____  
    / \ | | | | |      / \  / ___| 
   / _ \| | | | |     / _ \ \___ \ 
  / ___ \ |_| | |___ / ___ \ ___) |
 /_/   \_\___/|_____/_/   \_\____/ 
                                   
""")
        print("1. Listar aulas")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_aulas(lista_aulas)
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

menu_aula()