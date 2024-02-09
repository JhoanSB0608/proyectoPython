import json

def realizar_matricula():
    id_camper = int(input("Ingrese el ID del camper a matricular: "))
    
    camper_matricular = None
    for camper in campers_list:
        if camper.get('id') == id_camper and camper.get('estado') == 'aprobado':
            camper_matricular = camper
            break
    if not camper_matricular:
        print("Camper no encontrado o no aprobado.")
        return
    
    print("Rutas de entrenamiento disponibles:")
    for aula in lista_aulas:
        print(f"{aula['ruta_asignada']} - Capacidad: {aula['capacidad_actual']}/{aula['capacidad_maxima']}")

    ruta_asignada = input("Seleccione la ruta de entrenamiento para la matrícula: ")
    fecha_inicio_str = input("Ingrese la fecha de inicio (formato DD/MM/YYYY): ")
    fecha_finalizacion_str = input("Ingrese la fecha de finalización (formato DD/MM/YYYY): ")
    salon_entrenamiento = input("Ingrese el salón de entrenamiento: ")
    trainer_encargado = input("Ingrese el nombre del Trainer encargado: ")

    matricula = {
        'ruta_asignada': ruta_asignada,
        'fecha_inicio': fecha_inicio_str,
        'fecha_finalizacion': fecha_finalizacion_str,
        'salon_entrenamiento': salon_entrenamiento,
        'trainer_encargado': trainer_encargado
    }

    camper_matricular['matricula'] = matricula
    camper_matricular['estado_matricula'] = 'matriculado'

    for aula in lista_aulas:
        if aula['ruta_asignada'] == ruta_asignada:
            aula['capacidad_actual'] += 1
    print("Matrícula realizada con éxito.")

def cargar_datos_desde_json(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        print(f"Error al cargar datos desde JSON: {e}")
        return {}

def guardar_datos_en_json(nombre_archivo, data):
    with open(nombre_archivo, 'w') as file:
        json.dump(data, file, indent=4)
        
campers_list = cargar_datos_desde_json("campers.json") or []
lista_aulas = cargar_datos_desde_json("salasEntreno.json") or []

def matricula():
    while True:
        print(""" 
  __  __    _  _____ ____  ___ ____ _   _ _        _    
 |  \/  |  / \|_   _|  _ \|_ _/ ___| | | | |      / \   
 | |\/| | / _ \ | | | |_) || | |   | | | | |     / _ \  
 | |  | |/ ___ \| | |  _ < | | |___| |_| | |___ / ___ \ 
 |_|  |_/_/   \_\_| |_| \_\___\____|\___/|_____/_/   \_\                                                                                                               
 """)
        print("1. Registrar Datos")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            realizar_matricula()
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
        matricula()