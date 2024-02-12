import json

class PruebasDeSeleccion:
    def __init__(self, nombre, nota_teorica, nota_practica, promedio, estado):
        self.Nombre = nombre
        self.Nota_Teorica = nota_teorica
        self.Nota_Practica = nota_practica
        self.Promedio = promedio
        self.Estado = estado

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
        return data if isinstance(data, list) else []
    except json.JSONDecodeError as e:
        print(f"Error al cargar datos desde JSON: {e}")
        return []

def guardar_datos_en_json(nombre_archivo, data):
    with open(nombre_archivo, 'w') as file:
        json.dump(data, file, indent=4)

def rutas_entrenamiento_existentes():
    print("Rutas de entrenamiento existentes:")
    rutas_disponibles = ["Ruta NodeJS", "Ruta Java", "Ruta NetCore"]
    for ruta in rutas_disponibles:
        print("-", ruta)

def crear_ruta_nueva():
    nombre_ruta = input("Ingrese el nombre de la nueva ruta: ")
    sgdb_principal = input("Ingrese el SGDB principal: ")
    sgdb_alternativo = input("Ingrese el SGDB alternativo: ")
    modulos = input("Ingrese los módulos separados por coma: ").split(",")
    nueva_ruta = RutaEntrenamiento(nombre_ruta, sgdb_principal, sgdb_alternativo, modulos)
    rutas_entrenamiento_list.append(nueva_ruta)
    guardar_datos_en_json("data/rutas_entrenamiento.json", [ruta.__dict__ for ruta in rutas_entrenamiento_list])
    print("Nueva ruta creada exitosamente.")

def registro_notas_prueba():
    nombre_camper = input("Nombre del camper inscrito: ")
    nota_teorica = float(input("Nota teórica: "))
    nota_practica = float(input("Nota práctica: "))
    promedio = (nota_teorica + nota_practica) / 2
    estado = "Aprobado" if promedio >= 60 else "Reprobado"
    nueva_prueba = PruebasDeSeleccion(nombre_camper, nota_teorica, nota_practica, promedio, estado)
    pruebas_list.append(nueva_prueba)
    guardar_datos_en_json("data/pruebas.json", [prueba.__dict__ for prueba in pruebas_list])
    print("Registro de notas exitoso.")

def asignacion_rutas_entrenamiento():
    horario = input("Ingrese el horario (mañana/tarde): ")
    disponibles = []
    asignados = []

    if horario == "mañana":
        for ruta in rutas_entrenamiento_list:
            disponibles.append(ruta)

        for matricula in matriculas_list:
            if matricula["Horario_Entrenador"] == "tarde":
                ruta_tarde = next((ruta for ruta in rutas_entrenamiento_list if ruta.Nombre == matricula.Codigo_Ruta), None)
                if ruta_tarde in disponibles:
                    disponibles.remove(ruta_tarde)
                asignados.append(matricula)

    elif horario == "tarde":
        for ruta in rutas_entrenamiento_list:
            disponibles.append(ruta)

        for matricula in matriculas_list:
            if matricula["Horario_Entrenador"] == "mañana":
                ruta_manana = next((ruta for ruta in rutas_entrenamiento_list if ruta.Nombre == matricula.Codigo_Ruta), None)
                if ruta_manana in disponibles:
                    disponibles.remove(ruta_manana)
                asignados.append(matricula)

    print("Rutas disponibles:")
    for i, ruta in enumerate(disponibles, 1):
        print(f"{i}. {ruta.Nombre}")

    while True:
        opcion = input("Seleccione la ruta a asignar (ingrese el número correspondiente): ")
        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= len(disponibles):
                break
            else:
                print("Opción fuera de rango. Intente de nuevo.")
        else:
            print("Entrada no válida. Por favor, ingrese un número válido.")

    ruta_seleccionada = disponibles[opcion - 1]

    # Asignar campers y trainer a la ruta seleccionada
    # (Implementar la lógica de asignación de campers y trainers a la ruta seleccionada)

def asignacion_areas_entrenamiento():
    horario = input("Ingrese el horario (mañana/tarde): ")
    disponibles = []
    asignados = []

    if horario == "mañana":
        for area in areas_entrenamiento_list:
            disponibles.append(area)

        for matricula in matriculas_list:
            if matricula["Horario_Entrenador"] == "tarde":
                area_tarde = next((area for area in areas_entrenamiento_list if area.Nombre == matricula.Salon_Entrenamiento), None)
                if area_tarde in disponibles:
                    disponibles.remove(area_tarde)
                asignados.append(matricula)

    elif horario == "tarde":
        for area in areas_entrenamiento_list:
            disponibles.append(area)

        for matricula in matriculas_list:
            if matricula["Horario_Entrenador"] == "mañana":
                area_manana = next((area for area in areas_entrenamiento_list if area.Nombre == matricula.Salon_Entrenamiento), None)
                if area_manana in disponibles:
                    disponibles.remove(area_manana)
                asignados.append(matricula)

    print("Áreas de entrenamiento disponibles:")
    for i, area in enumerate(disponibles, 1):
        print(f"{i}. {area.Nombre}")

    opcion = int(input("Seleccione el área a asignar: "))
    area_seleccionada = disponibles[opcion - 1]

    # Asignar campers y trainer al área seleccionada
    # (Implementar la lógica de asignación de campers y trainers al área seleccionada)

def menu_coordinacion():
    print(""" 
  __  __ _____ _   _ _   _       ____   _    ____      _           ____ ___   ___  ____  ____ ___ _   _    _    ____ ___ ___  _   _ 
 |  \/  | ____| \ | | | | |     |  _ \ / \  |  _ \    / \         / ___/ _ \ / _ \|  _ \|  _ \_ _| \ | |  / \  / ___|_ _/ _ \| \ | |
 | |\/| |  _| |  \| | | | |     | |_) / _ \ | |_) |  / _ \       | |  | | | | | | | |_) | | | | ||  \| | / _ \| |    | | | | |  \| |
 | |  | | |___| |\  | |_| |     |  __/ ___ \|  _ <  / ___ \      | |__| |_| | |_| |  _ <| |_| | || |\  |/ ___ \ |___ | | |_| | |\  |
 |_|  |_|_____|_| \_|\___/      |_| /_/   \_\_| \_\/_/   \_\      \____\___/ \___/|_| \_\____/___|_| \_/_/   \_\____|___\___/|_| \_|
                                                                                                                                    
 """)
    print("1. Rutas de entrenamiento existentes")
    print("2. Crear Ruta Nueva")
    print("3. Registro de Notas para la Prueba")
    print("4. Asignación de Rutas de Entrenamiento para Campers Aprobados y Trainers")
    print("5. Asignación de Áreas de Entrenamiento para Trainer y Campers Inscritos")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")
 
    if opcion == "1":
        rutas_entrenamiento_existentes()
    elif opcion == "2":
        crear_ruta_nueva()
    elif opcion == "3":
        registro_notas_prueba()
    elif opcion == "4":
        asignacion_rutas_entrenamiento()
    elif opcion == "5":
        asignacion_areas_entrenamiento()
    elif opcion == "6":
        print("¡Hasta luego!")

campers_list = cargar_datos_desde_json("data/campers.json") or []
pruebas_list = cargar_datos_desde_json("data/pruebaSeleccion.json") or []
areas_entrenamiento_list = cargar_datos_desde_json("data/salasEntreno.json") or []
rutas_entrenamiento_list = cargar_datos_desde_json("data/rutas.json") or []
entrenadores_list = cargar_datos_desde_json("data/entrenadores.json") or []
matriculas_list = cargar_datos_desde_json("data/matriculas.json") or []
evaluaciones_modulo_list = cargar_datos_desde_json("data/evaluaciones_modulo.json") or []

if __name__ == "__main__":
    menu_coordinacion()