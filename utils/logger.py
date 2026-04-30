from datetime import datetime

def log_error(mensaje):
    with open("data/logs.txt", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] ERROR: {mensaje}\n")