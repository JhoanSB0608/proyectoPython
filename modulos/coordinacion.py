import json
from datetime import datetime

class PruebasDeSeleccion:
    def __init__(self, id, fecha, nota_teorica, nota_practica):
        self.N_Identificacion = id
        self.Fecha = fecha
        self.Nota_Teorica = nota_teorica
        self.Nota_Practica = nota_practica

class AreaEntrenamiento:
    def __init__(self, nombre, capacidad_maxima):
        self.Nombre = nombre
        self.Capacidad_Maxima = capacidad_maxima
        self.Campers = []

class RutaEntrenamiento:
    def __init__(self, nombre, sgdb_principal, sgdb_alternativo, modulos):
        self.Nombre = nombre
        self.SGDB_Principal = sgdb_principal
        self.SGDB_Alternativo = sgdb_alternativo
        self.Modulos = modulos

class Matricula:
    def __init__(self, id_camper, id_entrenador, id_ruta, fecha_inicio, fecha_fin, salon_entrenamiento):
        self.N_Identificacion_Camper = id_camper
        self.N_Identificacion_Entrenador = id_entrenador
        self.Codigo_Ruta = id_ruta
        self.Fecha_Inicio = fecha_inicio
        self.Fecha_Fin = fecha_fin
        self.Salon_Entrenamiento = salon_entrenamiento

class EvaluacionModulo:
    def __init__(self, id_camper, id_modulo, nota_teorica, nota_practica, quices, trabajos):
        self.N_Identificacion_Camper = id_camper
        self.Codigo_Modulo = id_modulo
        self.Nota_Teorica = nota_teorica
        self.Nota_Practica = nota_practica
        self.Quices = quices
        self.Trabajos = trabajos

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

def asignar_camper_a_ruta():
    id_camper = int(input("Ingrese el número de identificación del Camper: "))
    id_ruta = int(input("Ingrese el código de la ruta de entrenamiento: "))
    asignar_ruta(id_camper, id_ruta)

def asignar_ruta(id_camper, id_ruta):
    # Implementar lógica de asignación de ruta aquí
    pass

def asignar_notas(id_camper, id_modulo):
    # Implementar lógica de asignación de notas aquí
    pass

def asignar_notas_a_camper():
    id_camper = int(input("Ingrese el número de identificación del Camper: "))
    id_modulo = int(input("Ingrese el código del módulo: "))
    asignar_notas(id_camper, id_modulo)

def asignar_estado_a_camper(campers_list):
    id_camper = int(input("Ingrese el número de identificación del Camper: "))
    nuevo_estado = input("Ingrese el nuevo estado del Camper: ")
    
    for camper in campers_list:
        if camper["N_Identificacion"] == id_camper:
            camper["Estado"] = nuevo_estado
            guardar_datos_en_json("campers.json", campers_list)
            print("Estado actualizado exitosamente.")
            break
    else:
        print("Camper no encontrado.")

def asignar_salon(id_camper, id_ruta, matriculas_list):
    salon_entrenamiento = input("Ingrese el salón de entrenamiento: ")
    for matricula in matriculas_list:
        if matricula["N_Identificacion_Camper"] == id_camper and matricula["Codigo_Ruta"] == id_ruta:
            matricula["Salon_Entrenamiento"] = salon_entrenamiento
            print("Salón de entrenamiento asignado exitosamente.")
            guardar_datos_en_json("matriculas.json", matriculas_list)
            break
    else:
        print("Matrícula no encontrada para el Camper y ruta proporcionados.")

def asignar_trainer_y_horario(id_camper, id_ruta, matriculas_list):
    id_entrenador = input("Ingrese la identificación del entrenador: ")
    horario = input("Ingrese el horario del entrenador: ")
    for matricula in matriculas_list:
        if matricula["N_Identificacion_Camper"] == id_camper and matricula["Codigo_Ruta"] == id_ruta:
            matricula["N_Identificacion_Entrenador"] = id_entrenador
            matricula["Horario_Entrenador"] = horario
            print("Trainer y horario asignados exitosamente.")
            guardar_datos_en_json("matriculas.json", matriculas_list)
            break
    else:
        print("Matrícula no encontrada para el Camper y ruta proporcionados.")

def listar_campers_aprobados_inicial(evaluaciones_modulo_list, campers_list):
    nota_aprobacion = float(input("Ingrese la nota de aprobación inicial: "))
    for evaluacion in evaluaciones_modulo_list:
        if evaluacion["Nota_Teorica"] >= nota_aprobacion and evaluacion["Nota_Practica"] >= nota_aprobacion:
            camper = next((camper for camper in campers_list if camper["N_Identificacion"] == evaluacion["N_Identificacion_Camper"]), None)
            if camper:
                print(f"{camper['Nombre']} {camper['Apellido']} - {camper['N_Identificacion']} ha aprobado el examen inicial.")

def menu_coordinacion(campers_list, matriculas_list, evaluaciones_modulo_list):
    print(""" 
  __  __ _____ _   _ _   _       ____   _    ____      _           ____ ___   ___  ____  ____ ___ _   _    _    ____ ___ ___  _   _ 
 |  \/  | ____| \ | | | | |     |  _ \ / \  |  _ \    / \         / ___/ _ \ / _ \|  _ \|  _ \_ _| \ | |  / \  / ___|_ _/ _ \| \ | |
 | |\/| |  _| |  \| | | | |     | |_) / _ \ | |_) |  / _ \       | |  | | | | | | | |_) | | | | ||  \| | / _ \| |    | | | | |  \| |
 | |  | | |___| |\  | |_| |     |  __/ ___ \|  _ <  / ___ \      | |__| |_| | |_| |  _ <| |_| | || |\  |/ ___ \ |___ | | |_| | |\  |
 |_|  |_|_____|_| \_|\___/      |_| /_/   \_\_| \_\/_/   \_\      \____\___/ \___/|_| \_\____/___|_| \_/_/   \_\____|___\___/|_| \_|
                                                                                                                                    
 """)
    print("1. Asignar Camper a Ruta")
    print("2. Asignar Notas a Camper")
    print("3. Asignar Estado a Camper")
    print("4. Asignar Salón")
    print("5. Asignar Trainer y Horario")
    print("6. Listar Campers que Aprobaron el Examen Inicial")
    print("7. Salir")
    opcion = input("Seleccione una opción: ")
 
    if opcion == "1":
        asignar_camper_a_ruta()
    elif opcion == "2":
        asignar_notas_a_camper()
    elif opcion == "3":
        asignar_estado_a_camper(campers_list)
    elif opcion == "4":
        asignar_salon()
    elif opcion == "5":
        asignar_trainer_y_horario()
    elif opcion == "6":
        listar_campers_aprobados_inicial(evaluaciones_modulo_list, campers_list)
    elif opcion == "7":
        print("¡Hasta luego!")

campers_list = cargar_datos_desde_json("campers.json") or []
pruebas_list = cargar_datos_desde_json("pruebaSeleccion.json") or []
areas_entrenamiento_list = cargar_datos_desde_json("salasEntreno.json") or []
rutas_entrenamiento_list = cargar_datos_desde_json("rutas.json") or []
entrenadores_list = cargar_datos_desde_json("entrenadores.json") or []
matriculas_list = cargar_datos_desde_json("matriculas.json") or []
evaluaciones_modulo_list = cargar_datos_desde_json("evaluaciones_modulo.json") or []

while True:
    print("\n== Menú Principal ==")
    print("1. Menú de Coordinación")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        menu_coordinacion(campers_list, matriculas_list, evaluaciones_modulo_list)