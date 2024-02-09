import json

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

def guardar_datos(nombre_archivo, data):
    try:
        with open(nombre_archivo, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Los datos han sido guardados en el archivo {nombre_archivo}")
    except Exception as e:
        print(f"Error al guardar los datos en el archivo {nombre_archivo}: {e}")

def crear_aula(lista_aulas):
    if isinstance(lista_aulas, dict):
        lista_aulas = [lista_aulas] 

    nombre_aula = input("Ingrese el nombre del aula: ")
    asignar_ruta = input("Ingrese la ruta de entrenamiento asignada al aula: ").lower()

    aula = {
        "Nombre": nombre_aula,
        "Capacidad_Maxima": 33,
        "Capacidad_Actual": 0,
        "Ruta_Asignada": asignar_ruta
    }

    lista_aulas.append(aula)
    print("Se creó el aula con éxito.")
    guardar_datos("data/aulas.json", lista_aulas)


def listar_aulas(lista_aulas):
    print("Listado de aulas de entrenamiento: ")
    for aula in lista_aulas:
        print(aula)

def asignar_camper_a_ruta(lista_campers, lista_aulas):
    id_camper = int(input("Ingrese el ID del camper: "))
    asignar_ruta = input("Seleccione la ruta de entrenamiento para el camper: ").lower()

    for camper in lista_campers:
        if camper.get('estado') == 'aprobado' and camper.get('id') == id_camper:
            for aula in lista_aulas:
                if asignar_ruta == aula.get('Ruta_Asignada'):
                    if aula.get('Capacidad_Actual') < aula.get('Capacidad_Maxima'):
                        camper['ruta_asignada'] = asignar_ruta
                        aula['Capacidad_Actual'] += 1
                        guardar_datos("salasEntreno.json", lista_aulas)
                        print(f"Camper asignado a la ruta {asignar_ruta}.")
                        return
                    else:
                        print(f"No hay espacios disponibles en la ruta {asignar_ruta}")
                        return
    print(f"Ruta de entrenamiento {asignar_ruta} no encontrada o camper no aprobado")

def asignar_trainer_a_ruta(lista_trainers, lista_aulas):
    id_trainer = int(input("Ingrese el ID del trainer para asignarle una ruta de entrenamiento: "))
    asignar_ruta_trainer = input("Ingrese la ruta de entrenamiento que imparte el trainer: ")

    for aula in lista_aulas:
        if asignar_ruta_trainer == aula.get('Ruta_Asignada'):
            for trainer in lista_trainers:
                if not trainer.get('ruta_asignada') and trainer.get('id') == id_trainer:
                    trainer['ruta_asignada'] = asignar_ruta_trainer

                    if 'trainers_asignados' not in aula:
                        aula['trainers_asignados'] = []

                    aula['trainers_asignados'].append({
                        "Nombre": trainer['Nombre'],
                        "Apellidos": trainer['Apellidos']
                    })

                    guardar_datos("salasEntreno.json", lista_aulas)
                    print(f"Trainer ha sido asignado a la ruta {asignar_ruta_trainer}.")
                    return
                else:
                    print("El trainer ya está asignado a una ruta.")
                    return
    print(f"No existe la ruta {asignar_ruta_trainer}.")

def menu_aula():
    lista_aulas = cargar_datos("salasEntreno.json")
    lista_campers = []
    lista_trainers = []

    while True:
        print("\n--- Menú ---")
        print("1. Crear aula")
        print("2. Listar aulas")
        print("3. Asignar camper a ruta")
        print("4. Asignar trainer a ruta")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_aula(lista_aulas)
        elif opcion == "2":
            listar_aulas(lista_aulas)
        elif opcion == "3":
            asignar_camper_a_ruta(lista_campers, lista_aulas)
        elif opcion == "4":
            asignar_trainer_a_ruta(lista_trainers, lista_aulas)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

menu_aula()