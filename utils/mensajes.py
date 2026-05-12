# Formatea un mensaje agregando
# el tipo correspondiente
def _formatear(tipo, mensaje):
    return f"\n[{tipo}] {mensaje}"


# Imprime una línea separadora
# para mejorar la visualización en consola
def _separador():
    print("\n" + "=" * 40)

# Muestra mensajes de error
def mostrar_error(mensaje):
    print(_formatear("ERROR", mensaje))
    _separador()

# Muestra mensajes de éxito
def mostrar_ok(mensaje):
    print(_formatear("OK", mensaje))
    _separador()

# Muestra mensajes informativos
def mostrar_info(mensaje):
    print(_formatear("INFO", mensaje))
    _separador()

# Muestra mensajes de advertencia
def mostrar_warning(mensaje):
    print(_formatear("WARNING", mensaje))
    _separador()