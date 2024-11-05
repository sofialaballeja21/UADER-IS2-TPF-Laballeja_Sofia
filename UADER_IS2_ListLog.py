import json
from CorporateLog import CorporateLog
from decimal import Decimal

# Función para manejar Decimals
def custom_encoder(obj):
    if isinstance(obj, Decimal):
        return float(obj)  # Convertir Decimal a float
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

def list_all_logs():
    log_instance = CorporateLog.getInstance()
    logs = log_instance.listar_logs_por_cpu()  # Llama al método que lista los registros por CPU
    
    return logs

if __name__ == '__main__':
    logs = list_all_logs()  # Llama a la función y guarda el resultado
    if logs:
        # Convertir el string JSON de logs a un diccionario Python
        logs_dict = json.loads(logs)
        # Imprime los logs en formato JSON, usando custom_encoder para manejar Decimals
        print(json.dumps(json.loads(logs), default=custom_encoder, indent=4))
    else:
        print("No se encontraron registros en la tabla.")




   
