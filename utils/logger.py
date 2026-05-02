from datetime import datetime

RUTA_LOG = "data/logs.txt"

def _escribir_log(nivel, mensaje, accion="N/A"):
    """
    Función interna para escribir logs con formato estándar.
    ejemplo de formato: [2024-06-01 12:00:00] [ERROR] [ACCION: CREAR_CLIENTE] Detalles del error...
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(RUTA_LOG, "a") as file:
        file.write(f"[{timestamp}] [{nivel}] [ACCION: {accion}] {mensaje}\n")

def log_error(mensaje, accion="GENERAL"):
    _escribir_log("ERROR", mensaje, accion)

def log_warning(mensaje, accion="GENERAL"):
    _escribir_log("WARNING", mensaje, accion)

def log_info(mensaje, accion="GENERAL"):
    _escribir_log("INFO", mensaje, accion)

def log_success(mensaje, accion="GENERAL"):
    _escribir_log("SUCCESS", mensaje, accion)