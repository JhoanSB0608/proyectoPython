import json

def registrar_notas_filtro(campers_list):
    id_camper = int(input("Ingrese el ID del camper: "))
    camper_encontrado = buscar_camper_por_id(campers_list, id_camper)

    if camper_encontrado:
        nota_teoria = obtener_nota("teórica")
        nota_practica = obtener_nota("práctica")
        notas_quices_trabajos = obtener_nota("de quices y trabajos")

        promedio_filtro = calcular_promedio(nota_teoria, nota_practica, notas_quices_trabajos)

        notas_filtro = {
            'teorica': nota_teoria,
            'practica': nota_practica,
            'quices_trabajos': notas_quices_trabajos,
            'promedio': promedio_filtro,
            'estado_filtro': 'aprobado' if promedio_filtro >= 60 else 'no aprobado'
        }

        camper_encontrado['notas_filtro'] = notas_filtro

        print(f"Notas de filtro registradas para el camper {camper_encontrado['nombre']} {camper_encontrado['apellidos']}.")
        print(f"Nota Teórica: {nota_teoria}, Nota Práctica: {nota_practica}, Promedio: {promedio_filtro}")

        guardar_json(campers_list)
    else:
        print("Camper no encontrado.")

def buscar_camper_por_id(campers_list, id_camper):
    for camper in campers_list:
        if camper.get('id') == id_camper:
            return camper
    return None

def obtener_nota(tipo):
    return float(input(f"Ingrese la nota {tipo} para el filtro: "))

def calcular_promedio(teoria, practica, quices_trabajos):
    return 0.3 * teoria + 0.6 * practica + 0.1 * quices_trabajos

def guardar_json(campers_list):
    try:
        with open("data/campers.json", 'w') as file:
            json.dump(campers_list, file, indent=4)
        print("Datos guardados correctamente en el archivo campers.json")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def menu():
    campers_list = cargar_datos("data/campers.json")
    while True:
        print(""" 
  __  __ _____ _   _ _   _       ____   _    ____      _          _____ ___ _   _____ ____   ___  ____  
 |  \/  | ____| \ | | | | |     |  _ \ / \  |  _ \    / \        |  ___|_ _| | |_   _|  _ \ / _ \/ ___| 
 | |\/| |  _| |  \| | | | |     | |_) / _ \ | |_) |  / _ \       | |_   | || |   | | | |_) | | | \___ \ 
 | |  | | |___| |\  | |_| |     |  __/ ___ \|  _ <  / ___ \      |  _|  | || |___| | |  _ <| |_| |___) |
 |_|  |_|_____|_| \_|\___/      |_| /_/   \_\_| \_\/_/   \_\     |_|   |___|_____|_| |_| \_\\___/|____/ 
                                                                                                        
""")
        print("1. Registrar notas de filtro")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_notas_filtro(campers_list)
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def cargar_datos(archivo):
    try:
        with open(archivo, 'r') as f:
            datos = json.load(f)
        print(f"Los datos del archivo {archivo} han sido cargados")
        return datos
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {archivo}. El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido al cargar el archivo {archivo}: {e}")
        return []

if __name__ == "__main__":
    menu()