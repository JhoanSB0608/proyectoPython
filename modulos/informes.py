import json

def menu_informes():
    print(""" 
  __  __ _____ _   _ _   _       ____  _____       ___ _   _ _____ ___  ____  __  __ _____ ____  
 |  \/  | ____| \ | | | | |     |  _ \| ____|     |_ _| \ | |  ___/ _ \|  _ \|  \/  | ____/ ___| 
 | |\/| |  _| |  \| | | | |     | | | |  _|        | ||  \| | |_ | | | | |_) | |\/| |  _| \___ \ 
 | |  | | |___| |\  | |_| |     | |_| | |___       | || |\  |  _|| |_| |  _ <| |  | | |___ ___) |
 |_|  |_|_____|_| \_|\___/      |____/|_____|     |___|_| \_|_|   \___/|_| \_\_|  |_|_____|____/ 
                                                                                                 
 """)
    print("1. Listar Campers en Estado de Inscrito")
    print("2. Listar Campers que Aprobaron el Examen Inicial")
    print("3. Listar Entrenadores Trabajando en CampusLands")
    print("4. Listar Campers con Bajo Rendimiento")
    print("5. Listar Campers y Entrenador Asociados a una Ruta de Entrenamiento")
    print("6. Mostrar Campers que Aprobaron y Perdieron cada Módulo")
    print("7. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        listar_campers_inscritos()
    elif opcion == "2":
        listar_campers_aprobados_inicial()
    elif opcion == "3":
        listar_entrenadores_trabajando()
    elif opcion == "4":
        listar_campers_bajo_rendimiento()
    elif opcion == "5":
        listar_campers_y_entrenador_ruta()
    elif opcion == "6":
        mostrar_aprobados_y_perdidos_modulos()
    elif opcion == "7":
        print("¡Hasta luego!")

def listar_campers_inscritos():
    for camper in campers_list:
        if camper["Estado"] == "Inscrito":
            print(f"{camper['Nombre']} {camper['Apellido']} - {camper['N_Identificacion']}")

def listar_campers_aprobados_inicial():
    # Implementa la lógica para listar campers que aprobaron el examen inicial
    pass

def listar_entrenadores_trabajando():
    # Implementa la lógica para listar entrenadores que están trabajando en CampusLands
    pass

def listar_campers_bajo_rendimiento():
    # Implementa la lógica para listar campers con bajo rendimiento
    pass

def listar_campers_y_entrenador_ruta():
    # Implementa la lógica para listar campers y entrenador asociados a una ruta de entrenamiento
    pass

def mostrar_aprobados_y_perdidos_modulos():
    # Implementa la lógica para mostrar cuántos campers aprobaron y perdieron cada módulo
    pass

# Cargar datos existentes o inicializar estructuras de datos vacías
def cargar_datos_desde_json(archivo):
    try:
        with open(archivo, 'r') as file:
            datos = json.load(file)
        return datos
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe.")
        return None
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo {archivo}.")
        return None
    
campers_list = cargar_datos_desde_json("campers.json") or []
pruebas_list = cargar_datos_desde_json("pruebas.json") or []
areas_entrenamiento_list = cargar_datos_desde_json("areas_entrenamiento.json") or []
rutas_entrenamiento_list = cargar_datos_desde_json("rutas_entrenamiento.json") or []
entrenadores_list = cargar_datos_desde_json("entrenadores.json") or []
matriculas_list = cargar_datos_desde_json("matriculas.json") or []
evaluaciones_modulo_list = cargar_datos_desde_json("evaluaciones_modulo.json") or []