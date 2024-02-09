import modulos.camper as camper
import modulos.coordinacion as coordinacion
import modulos.trainer as trainer
import modulos.informes as informes
import modulos.matricula as matricula
import modulos.rutasEntrenamiento as rutasEntrenamiento
import modulos.filtros as filtros

def menu_principal():
    while True:
        print("\nBienvenido al Sistema de Gestión de CampusLands")
        print("1. Menú de Campers")
        print("2. Menú de Trainer")
        print("3. Matricula")
        print("4. Menú de Coordinación")
        print("5. Asignar Ruta")
        print("6. Asignar Aula")
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