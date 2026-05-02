def obtener_opcion(mensaje, opciones_validas):
    """
    Solicita una opción al usuario hasta que sea válida.
    :param mensaje: Texto a mostrar al usuario
    :param opciones_validas: Lista de opciones válidas (ej: ["1","2","3"])
    :return: Opción válida
    """
    while True:
        opcion = input(mensaje).strip()
        print()

        if opcion in opciones_validas:
            return opcion

        print(f"[ERROR] Opción inválida. Opciones válidas: {', '.join(opciones_validas)}")