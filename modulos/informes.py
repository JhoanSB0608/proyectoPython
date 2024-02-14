import json

def listar_campers_inscritos():
    for camper in campers_list:
        if camper["Estado"] == "Inscrito":
            print(f"{camper['Nombre']} {camper['Apellidos']} - {camper['Nro_Identificacion']}")

def listar_campers_aprobados_inicial():
    print("+ Todos los campers que aprobaron el examen inicial:")
    for prueba in pruebas_list:
        if prueba["Estado"] == "Aprobado":
            print(f"{prueba['Nombre']} - Nota Teórica: {prueba['Nota_Teorica']}, Nota Práctica: {prueba['Nota_Practica']}")

def listar_entrenadores_trabajando():
    print("+ Todos los entrenadores que trabajan en Campus:")
    for entrenador in entrenadores_list:
        print(entrenador['Nombre'])

def listar_campers_bajo_rendimiento():
    print("+ Todos los campers que tienen un promedio bajo:")
    for prueba in pruebas_list:
        promedio = (prueba["Nota_Teorica"] + prueba["Nota_Practica"]) / 2
        if promedio < 60:
            print(f"{prueba['Nombre']} - Promedio: {promedio}")

def listar_camper_y_entrenador_en_ruta():
    print("+ Camper y entrenador en ruta de entrenamiento:")
    for ruta in rutas_entrenamiento_list:
        print(f"\n{ruta['Nombre']}:")
        for horario, asignaciones in ruta["Asignaciones"].items():
            print(f"\n{horario}:")
            for asignacion in asignaciones:
                print(f"+ Trainer: {asignacion['Entrenador']}")
                print("  Campers:")
                for camper in asignacion['Campers']:
                    print(f"    - {camper}")

def listar_aprobaciones_por_modulo():
    for ruta in rutas_entrenamiento_list:
        print(f"\nRuta de Entrenamiento: {ruta['Nombre']}")
        for asignacion in ruta.get("Asignaciones", []):
            entrenador = asignacion.get("Entrenador", "")
            print(f"\nEntrenador: {entrenador}")
            for modulo, campers in asignacion.get("Campers_por_modulo", {}).items():
                aprobados = 0
                perdidos = 0
                for camper in campers:
                    prueba_camper = next((p for p in pruebas_list if p["Nombre"] == camper), None)
                    if prueba_camper:
                        promedio = (prueba_camper["Nota_Teorica"] + prueba_camper["Nota_Practica"]) / 2
                        if promedio >= 60:
                            aprobados += 1
                        else:
                            perdidos += 1
                print(f"\nMódulo: {modulo}")
                print(f"Cantidad de Campers Aprobados: {aprobados}")
                print(f"Cantidad de Campers Perdidos: {perdidos}")

def menu_informes():
    print(""" 
  __  __ _____ _   _ _   _       ____  _____       ___ _   _ _____ ___  ____  __  __ _____ ____  
 |  \/  | ____| \ | | | | |     |  _ \| ____|     |_ _| \ | |  ___/ _ \|  _ \|  \/  | ____/ ___| 
 | |\/| |  _| |  \| | | | |     | | | |  _|        | ||  \| | |_ | | | | |_) | |\/| |  _| \___ \ 
 | |  | | |___| |\  | |_| |     | |_| | |___       | || |\  |  _|| |_| |  _ <| |  | | |___ ___) |
 |_|  |_|_____|_| \_|\___/      |____/|_____|     |___|_| \_|_|   \___/|_| \_\_|  |_|_____|____/ 
                                                                                                 
 """)
    print("1. Campers inscritos")
    print("2. Campers que aprobaron el examen inicial")
    print("3. Entrenadores trabajando")
    print("4. Campers de bajo rendimiento")
    print("5. Camper y entrenador en ruta entrenamiento")
    print("6. Aprobaciones por Módulo")
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
        listar_camper_y_entrenador_en_ruta()
    elif opcion == "6":
        listar_aprobaciones_por_modulo()
    elif opcion == "7":
        print("¡Hasta luego!")

def cargar_datos_desde_json(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as file:
            data = json.load(file)
            if nombre_archivo == "data/rutas_entrenamiento.json":
                for ruta in data:
                    ruta["Asignaciones"] = {}  
        return data
    except json.JSONDecodeError as e:
        print(f"Error al cargar datos desde JSON: {e}")
        return {}
    
campers_list = cargar_datos_desde_json("data/campers.json") or []
pruebas_list = cargar_datos_desde_json("data/pruebaSeleccion.json") or []
entrenadores_list = cargar_datos_desde_json("data/entrenadores.json") or []
rutas_entrenamiento_list = cargar_datos_desde_json("data/rutas_entrenamiento.json") or []

if __name__ == "__main__":
    menu_informes()