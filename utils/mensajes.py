def _formatear(tipo, mensaje):
    return f"\n[{tipo}] {mensaje}"

def _separador():
    print("\n" + "=" * 40)

def mostrar_error(mensaje):
    print(_formatear("ERROR", mensaje))
    _separador()


def mostrar_ok(mensaje):
    print(_formatear("OK", mensaje))
    _separador()

def mostrar_info(mensaje):
    print(_formatear("INFO", mensaje))
    _separador()

