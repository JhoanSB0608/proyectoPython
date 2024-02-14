import modulos.camper as camper
import modulos.coordinacion as coordinacion
import modulos.trainer as trainer
import modulos.informes as informes
import modulos.matricula as matricula
import modulos.rutasEntrenamiento as rutasEntrenamiento
import modulos.filtros as filtros

def menu_principal():
    while True:
        print(""" 
  ____  _                           _     _                 _     ____  _     _                               _        
 | __ )(_) ___ _ ____   _____ _ __ (_) __| | ___       __ _| |   / ___|(_)___| |_ ___ _ __ ___   __ _      __| | ___   
 |  _ \| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \     / _` | |   \___ \| / __| __/ _ \ '_ ` _ \ / _` |    / _` |/ _ \  
 | |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) |   | (_| | |    ___) | \__ \ ||  __/ | | | | | (_| |   | (_| |  __/  
 |____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/     \__,_|_|   |____/|_|___/\__\___|_| |_| |_|\__,_|    \__,_|\___|  
   ____           _   _                     _           ____                                _                    _     
  / ___| ___  ___| |_(_) ___  _ __       __| | ___     / ___|__ _ _ __ ___  _ __  _   _ ___| |    __ _ _ __   __| |___ 
 | |  _ / _ \/ __| __| |/ _ \| '_ \     / _` |/ _ \   | |   / _` | '_ ` _ \| '_ \| | | / __| |   / _` | '_ \ / _` / __|
 | |_| |  __/\__ \ |_| | (_) | | | |   | (_| |  __/   | |__| (_| | | | | | | |_) | |_| \__ \ |__| (_| | | | | (_| \__ \
  \____|\___||___/\__|_|\___/|_| |_|    \__,_|\___|    \____\__,_|_| |_| |_| .__/ \__,_|___/_____\__,_|_| |_|\__,_|___/
                                                                           |_|                                         
""")
        print("1. Menú de Campers")
        print("2. Menú de Trainer")
        print("3. Matricula")
        print("4. Menú de Coordinación")
        print("5. Rutas")
        print("6. Aulas")
        print("7. Filtros")
        print("8. Menú de Informes")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            from modulos import camper
            camper.menu()
        elif opcion == "2":
            from modulos import trainer
            trainer.main()
        elif opcion == "3":
            from modulos import matricula
            matricula.matricula()
        elif opcion == "4":
            from modulos import coordinacion
            coordinacion.menu_coordinacion()
        elif opcion == "5":
            from modulos import rutasEntrenamiento
            rutasEntrenamiento.menu() 
        elif opcion == "6":
            from modulos import aula
            aula.menu_aula()
        elif opcion == "7":
            from modulos import filtros
            filtros.menu()
        elif opcion == "8":
            from modulos import informes
            informes.menu_informes()
        elif opcion == "9":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()