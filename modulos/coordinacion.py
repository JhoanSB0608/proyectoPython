from datetime import datetime
import json

class PruebaSeleccion:
    def __init__(self, nombre, nota_teorica, nota_practica, promedio, estado):
        self.Nombre = nombre
        self.Nota_Teorica = nota_teorica
        self.Nota_Practica = nota_practica
        self.Promedio = promedio
        self.Estado = estado

    def to_dict(self):
        return {
            "Nombre": self.Nombre,
            "Nota_Teorica": self.Nota_Teorica,
            "Nota_Practica": self.Nota_Practica,
            "Promedio": self.Promedio,
            "Estado": self.Estado
        }

class AreaEntrenamiento:
    def __init__(self, nombre, capacidad_maxima):
        self.Nombre_Sala = nombre 
        self.Capacidad_Maxima = capacidad_maxima
        self.Campers = []
        self.Trainer = None

class RutaEntrenamiento:
    def __init__(self, nombre, modulos):
        self.Nombre = nombre
        self.Modulos = modulos
        self.Campers = []
        self.Trainer = None

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
        
        if "rutas_entrenamiento" in nombre_archivo:
            rutas = []
            for item in data:
                if isinstance(item, dict):
                    nombre = item.get('Nombre')
                    if nombre:
                        modulos = [
                            *item.get('Modulos', [])
                        ]
                        nueva_ruta = RutaEntrenamiento(nombre, modulos)
                        rutas.append(nueva_ruta)
                    else:
                        print("La ruta no tiene un nombre válido.")
                else:
                    print("El valor de la ruta no es un diccionario válido.")
            
            return rutas
        elif "salasEntreno" in nombre_archivo:
            areas = []
            for item in data:
                if isinstance(item, dict):
                    nombre_sala = item.get('Nombre_Sala')
                    if nombre_sala:
                        capacidad = item.get('Capacidad')
                        nueva_area = AreaEntrenamiento(nombre_sala, capacidad)
                        areas.append(nueva_area)
                    else:
                        print("El área no tiene un nombre válido.")
                else:
                    print("El valor del área no es un diccionario válido.")
            
            return areas
        else:
            print("El nombre del archivo no coincide con ningún tipo de datos conocido.")
            return []
    except json.JSONDecodeError as e:
        print(f"Error al cargar datos desde JSON: {e}")
        return []

def guardar_datos_en_json(nombre_archivo, data):
    with open(nombre_archivo, 'w') as file:
        json.dump(data, file, indent=4)

def rutas_entrenamiento_existentes():
    print("Rutas de entrenamiento existentes:")
    for ruta in rutas_entrenamiento_list:
        print("-", ruta.Nombre)

def areas_entrenamiento_disponibles():
    print("Áreas de entrenamiento disponibles:")
    for area in areas_entrenamiento_list:
        print("-", area.Nombre_Sala) 

def crear_ruta_nueva():
    nombre_ruta = input("Ingrese el nombre de la nueva ruta: ")
    modulos = input("Ingrese los módulos separados por coma: ").split(",")
    nueva_ruta = RutaEntrenamiento(nombre_ruta, modulos)
    rutas_entrenamiento_list.append(nueva_ruta)
    guardar_datos_en_json("data/rutas_entrenamiento.json", [ruta.__dict__ for ruta in rutas_entrenamiento_list])
    print("Nueva ruta creada exitosamente.")

def registro_notas_prueba():
    nombre_camper = input("Nombre del camper inscrito: ")
    nota_teorica = float(input("Nota teórica: "))
    nota_practica = float(input("Nota práctica: "))
    promedio = (nota_teorica + nota_practica) / 2
    estado = "Aprobado" if promedio >= 60 else "Reprobado"
    nueva_prueba = PruebaSeleccion(nombre_camper, nota_teorica, nota_practica, promedio, estado)
    pruebas_list.append(nueva_prueba.to_dict())
    guardar_datos_en_json("data/pruebaSeleccion.json", pruebas_list)
    print("Registro de notas exitoso.")

def asignar_campers_entrenador_a_ruta():
    rutas_entrenamiento_existentes()
    ruta_seleccionada = input("Ingrese el nombre de la ruta seleccionada: ")
    trainer_asignado = input("Ingrese el ID del entrenador asignado: ")
    campers_a_asignar = input("Ingrese los ID de los campers a asignar (separados por comas): ").split(",")

    for ruta in rutas_entrenamiento_list:
        if ruta.Nombre == ruta_seleccionada:
            for camper_id in campers_a_asignar:
                ruta.Campers.append(camper_id)
            ruta.Trainer = trainer_asignado
            guardar_datos_en_json("data/rutas_entrenamiento.json", [ruta.__dict__ for ruta in rutas_entrenamiento_list])
            print("Asignación exitosa.")
            return

    print("La ruta seleccionada no existe.")

def asignar_campers_entrenador_a_area():
    areas_entrenamiento_disponibles()
    area_seleccionada = input("Ingrese el nombre del área seleccionada: ")
    trainer_asignado = input("Ingrese el ID del entrenador asignado: ")
    campers_a_asignar = input("Ingrese los ID de los campers a asignar (separados por comas): ").split(",")

    for area in areas_entrenamiento_list:
        if area.Nombre_Sala == area_seleccionada: 
            for camper_id in campers_a_asignar:
                area.Campers.append(camper_id)
            area.Trainer = trainer_asignado
            guardar_datos_en_json("data/salasEntreno.json", [area.__dict__ for area in areas_entrenamiento_list])
            print("Asignación exitosa.")
            return

    print("El área seleccionada no existe.")

def elegir_horario():
    print("Horarios disponibles:")
    print("1. De 6:00 a.m a 9:00 a.m")
    print("2. De 10:00 a.m a 1:00 p.m")
    print("3. De 2:00 p.m a 5:00 p.m")
    print("4. De 6:00 p.m a 10:00 p.m")
    
    opcion = input("Seleccione un horario (1/2/3/4): ")
    
    if opcion == "1":
        return "De 6:00 a.m a 9:00 a.m"
    elif opcion == "2":
        return "De 10:00 a.m a 1:00 p.m"
    elif opcion == "3":
        return "De 2:00 p.m a 5:00 p.m"
    elif opcion == "4":
        return "De 6:00 p.m a 10:00 p.m"
    else:
        print("Opción inválida. Inténtelo de nuevo.")
        return elegir_horario()

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
    print("4. Elegir Horario")
    print("5. Asignación de Rutas de Entrenamiento para Campers Aprobados y Trainers")
    print("6. Asignación de Áreas de Entrenamiento para Trainer y Campers Inscritos")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")
 
    if opcion == "1":
        rutas_entrenamiento_existentes()
    elif opcion == "2":
        crear_ruta_nueva()
    elif opcion == "3":
        registro_notas_prueba()
    elif opcion == "4":
        horario_elegido = elegir_horario()
        print("Horario elegido:", horario_elegido)
    elif opcion == "5":
        asignar_campers_entrenador_a_ruta()
    elif opcion == "6":
        asignar_campers_entrenador_a_area()
    elif opcion == "7":
        print("¡Hasta luego!")

campers_list = cargar_datos_desde_json("data/campers.json") or []
pruebas_list = cargar_datos_desde_json("data/pruebaSeleccion.json") or []
areas_entrenamiento_list = cargar_datos_desde_json("data/salasEntreno.json") or []
rutas_entrenamiento_list = cargar_datos_desde_json("data/rutas_entrenamiento.json") or []
entrenadores_list = cargar_datos_desde_json("data/entrenadores.json") or []
matriculas_list = cargar_datos_desde_json("data/matriculas.json") or []
evaluaciones_modulo_list = cargar_datos_desde_json("data/evaluaciones_modulo.json") or []

if __name__ == "__main__":
    menu_coordinacion()