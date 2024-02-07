import modulos.camper as camper

def menu_principal():
    while True:
        print("\nBienvenido al Sistema de Gestión de CampusLands")
        print("1. Menú de Campers")
        print("2. Menú de Trainer")
        print("3. Menú de Coordinación")
        print("4. Menú de Informes")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            from modulos import camper
            camper.menu()
        elif opcion == "2":
            from modulos import trainer
            trainer.main()
        elif opcion == "3":
            from modulos import coordinacion
            coordinacion.menu_coordinacion()
        elif opcion == "4":
            from modulos import informes
            informes.menu_informes()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()