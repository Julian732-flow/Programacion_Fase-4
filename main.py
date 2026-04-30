from views.menu import mostrar_menu

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            pass
        elif opcion == "4":
            break

if __name__ == "__main__":
    main()